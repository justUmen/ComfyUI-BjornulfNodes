import os
import time
import requests
from PIL import Image
import numpy as np
import torch

class APIGenerateFlux:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": "1ae1f1cc-de28-4682-bc4c-6ac2fdff79cc"
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful landscape"
                }),
                "model": (["flux-pro-1.1-ultra", "flux-pro-1.1", "flux-pro", "flux-dev"], {
                    "default": "flux-pro-1.1-ultra"
                }),
                "aspect_ratio": (["16:9", "1:1", "4:3", "3:2", "21:9", "9:21"], {
                    "default": "16:9"
                }),
                "width": ("INT", {
                    "default": 2752,
                    "min": 256,
                    "max": 2752,
                    "step": 32
                }),
                "height": ("INT", {
                    "default": 1536,
                    "min": 256,
                    "max": 1536,
                    "step": 32
                }),
                "output_format": (["png", "jpeg"], {
                    "default": "png"
                }),
            },
            "optional": {
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff
                }),
                "safety_tolerance": ("INT", {
                    "default": 6,
                    "min": 0,
                    "max": 6
                }),
                "raw": ("BOOLEAN", {
                    "default": False
                }),
                "image_prompt_strength": ("FLOAT", {
                    "default": 0.1,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01
                }),
                "steps": ("INT", {
                    "default": 50,
                    "min": 15,
                    "max": 50
                }),
                "guidance": ("FLOAT", {
                    "default": 2.5,
                    "min": 1.0,
                    "max": 100.0,
                    "step": 0.1
                }),
                "prompt_upsampling": ("BOOLEAN", {
                    "default": False
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate"
    CATEGORY = "BFL API"

    def get_next_number(self):
        save_dir = "output/API/BlackForestLabs"
        os.makedirs(save_dir, exist_ok=True)
        files = [f for f in os.listdir(save_dir) if f.endswith('.png')]
        if not files:
            return 1
        numbers = [int(f.split('.')[0]) for f in files]
        return max(numbers) + 1

    def generate(self, api_key, prompt, model, aspect_ratio, output_format, 
                seed=0, safety_tolerance=2, raw=False, image_prompt_strength=0.1,
                width=1024, height=768, steps=50, guidance=30.0, 
                prompt_upsampling=False):
        
        headers = {
            'accept': 'application/json',
            'x-key': api_key,
            'Content-Type': 'application/json'
        }

        # Base payload
        payload = {
            'prompt': prompt,
            'output_format': output_format,
            'safety_tolerance': safety_tolerance,
        }

        # Add model-specific parameters
        if model == "flux-pro-1.1-ultra":
            payload.update({
                'aspect_ratio': aspect_ratio,
                'raw': raw,
                'image_prompt_strength': image_prompt_strength
            })
            if seed != 0:
                payload['seed'] = seed
                
        else:  # Other models
            payload.update({
                'width': width,
                'height': height,
                'steps': steps,
                'guidance': guidance,
                'prompt_upsampling': prompt_upsampling
            })
            if seed != 0:
                payload['seed'] = seed

        # Make API request
        response = requests.post(
            f'https://api.bfl.ml/v1/{model}',
            headers=headers,
            json=payload
        )
        
        if response.status_code != 200:
            raise Exception(f"API request failed: {response.text}")

        request_id = response.json()['id']
        
        # Poll for results
        while True:
            time.sleep(0.5)
            result = requests.get(
                f"https://api.bfl.ml/v1/get_result?id={request_id}",
                headers=headers
            )
            
            if result.status_code != 200:
                raise Exception(f"Failed to get results: {result.text}")
                
            data = result.json()
            status = data['status']
            
            if status == "Ready":
                image_url = data['result']['sample']
                
                # Download and process image
                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    next_num = self.get_next_number()
                    filename = f"{next_num:03d}.png"
                    filepath = os.path.join("output/API/BlackForestLabs", filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(image_response.content)
                    
                    img = Image.open(filepath)
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    img_tensor = torch.from_numpy(np.array(img).astype(np.float32) / 255.0)
                    img_tensor = img_tensor.unsqueeze(0)
                    
                    return (img_tensor,)
                else:
                    raise Exception("Failed to download image")
                    
            elif status in ["Content Moderated", "Request Moderated"]:
                raise Exception(f"{status}. Process stopped.")
            
            print(f"Status: {status}")