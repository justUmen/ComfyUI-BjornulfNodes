import os
import time
import requests
from PIL import Image
import numpy as np
import torch
import fal_client
from io import BytesIO
import json
import threading
import asyncio

class APIGenerateFalAI:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_token": ("STRING", {
                    "multiline": False,
                    "default": "",
                    "display": "Fal.ai API Token"
                }),
                "model": (["fal-ai/flux-pro/v1.1-ultra", "fal-ai/recraft-v3", "fal-ai/flux-general/image-to-image"], {
                    "default": "fal-ai/flux-pro/v1.1-ultra"
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A blackhole in space"
                }),
                "number_of_images": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 10,
                    "step": 1
                }),
                "seed": ("INT", {
                    "default": -1,
                    "min": -1,
                    "max": 2147483647
                }),
                "timeout": ("INT", {
                    "default": 300,
                    "min": 60,
                    "max": 1800,
                    "step": 60,
                    "display": "Timeout (seconds)"
                }),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING",)
    RETURN_NAMES = ("image", "generation_info",)
    FUNCTION = "generate"
    CATEGORY = "FalAI"

    def __init__(self):
        self.output_dir = "output/API/FalAI"
        self.metadata_dir = "output/API/FalAI/metadata"
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.metadata_dir, exist_ok=True)
        self._interrupt_event = threading.Event()

    def get_next_number(self):
        save_dir = "output/API/FalAI"
        os.makedirs(save_dir, exist_ok=True)
        files = [f for f in os.listdir(save_dir) if f.endswith('.png')]
        if not files:
            return 1
        numbers = [int(f.split('.')[0]) for f in files]
        return max(numbers) + 1

    def create_filename(self, number):
        # Simply format the number with leading zeros
        return f"{number:03d}.png"

    def save_image_and_metadata(self, img, generation_info, number):
        # Create simple filename
        filename = self.create_filename(number)
        filepath = os.path.join(self.output_dir, filename)
        
        # Save image
        img.save(filepath)

        # Create metadata filename based on the image filename
        metadata_filename = f"{number:03d}_metadata.json"
        metadata_filepath = os.path.join(self.metadata_dir, metadata_filename)
        
        # Save metadata
        with open(metadata_filepath, 'w', encoding='utf-8') as f:
            json.dump(generation_info, f, indent=4, ensure_ascii=False)

        return filepath, metadata_filepath

    async def generate_single_image_async(self, input_data, api_token, model):
        try:
            # Set the environment variable for the API token
            os.environ['FAL_KEY'] = api_token
            
            # Submit request and get request ID
            handler = await fal_client.submit_async(
                model,
                arguments=input_data
            )
            request_id = handler.request_id
            print(f"Request ID: {request_id}")

            # Wait for the result
            result = await fal_client.result_async(model, request_id)
            
            if not result or 'images' not in result or not result['images']:
                raise ValueError(f"No valid result received. Result: {result}")

            # Get image URL and download image
            image_url = result['images'][0]['url']
            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                raise ConnectionError(f"Failed to download image: Status code {image_response.status_code}")

            # Process image
            img = Image.open(BytesIO(image_response.content))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Save metadata and image
            number = self.get_next_number()
            generation_info = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "parameters": input_data,
                "result": result,
                "request_id": request_id
            }
            
            image_path, metadata_path = self.save_image_and_metadata(img, generation_info, number)
            print(f"Saved image to: {image_path}")
            print(f"Saved metadata to: {metadata_path}")
            
            img_tensor = torch.from_numpy(np.array(img).astype(np.float32) / 255.0)
            img_tensor = img_tensor.unsqueeze(0)

            return img_tensor, generation_info

        except Exception as e:
            print(f"Generation error: {str(e)}")
            raise Exception(f"Error generating image: {str(e)}")

    def generate(self, api_token, model, prompt, number_of_images=1, seed=-1, timeout=300):
        if not api_token:
            raise ValueError("API token is required")
            
        self._interrupt_event.clear()
        empty_image = torch.zeros((1, 1024, 1024, 3))  # Default size
        
        try:
            images = []
            infos = []
            failed_jobs = []

            # Create new event loop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            async def process_all_images():
                tasks = []
                for i in range(number_of_images):
                    if self._interrupt_event.is_set():
                        break
                    
                    # Create input data for each image
                    input_data = {"prompt": prompt}
                    
                    # If seed is provided, increment it for each image
                    # If seed is -1, generate a random seed for each image
                    if seed != -1:
                        current_seed = seed + i
                    else:
                        current_seed = np.random.randint(0, 2147483647)
                    
                    input_data["seed"] = current_seed
                    tasks.append(self.generate_single_image_async(input_data, api_token, model))
                
                return await asyncio.gather(*tasks, return_exceptions=True)

            try:
                results = loop.run_until_complete(process_all_images())
            finally:
                loop.close()

            for result in results:
                if isinstance(result, Exception):
                    failed_jobs.append({
                        'error': str(result)
                    })
                else:
                    img_tensor, generation_info = result
                    images.append(img_tensor)
                    infos.append(generation_info)

            if not images:
                generation_info = {
                    "error": "All generation jobs failed",
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "failed_jobs": failed_jobs
                }
                return (empty_image, json.dumps(generation_info, indent=2))

            combined_tensor = torch.cat(images, dim=0)
            
            combined_info = {
                "successful_generations": len(images),
                "total_requested": number_of_images,
                "generation_parameters": {
                    "prompt": prompt,
                    "initial_seed": seed
                },
                "individual_results": infos,
                "failed_jobs": failed_jobs if failed_jobs else None
            }

            return (combined_tensor, json.dumps(combined_info, indent=2))

        except Exception as e:
            generation_info = {
                "error": f"Fal.ai generation failed: {str(e)}",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            return (empty_image, json.dumps(generation_info, indent=2))


    def recover_image_by_request_id(self, request_id, api_token, model):
        try:
            # Set the environment variable for the API token
            os.environ['FAL_KEY'] = api_token
            
            result = fal_client.result(model, request_id)
            if not result or 'images' not in result or not result['images']:
                raise ValueError(f"No valid result for request ID {request_id}")

            image_url = result['images'][0]['url']
            image_response = requests.get(image_url)
            if image_response.status_code != 200:
                raise ConnectionError(f"Failed to download image: Status code {image_response.status_code}")

            img = Image.open(BytesIO(image_response.content))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            number = self.get_next_number()
            generation_info = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "result": result,
                "request_id": request_id
            }
            
            image_path, metadata_path = self.save_image_and_metadata(img, generation_info, number)
            img_tensor = torch.from_numpy(np.array(img).astype(np.float32) / 255.0)
            img_tensor = img_tensor.unsqueeze(0)

            return img_tensor, generation_info

        except Exception as e:
            raise Exception(f"Error recovering image: {str(e)}")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def interrupt(self):
        print("Interrupting Fal.ai generation...")
        self._interrupt_event.set()