import os
import time
import requests
from PIL import Image
import numpy as np
import torch
import base64

class APIGenerateStability:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "A beautiful landscape"
                }),
            },
            "optional": {
                "negative_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "aspect_ratio": (["16:9", "1:1", "21:9", "2:3", "3:2", "4:5", "5:4", "9:16", "9:21"], {
                    "default": "1:1"
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 4294967294
                }),
                "output_format": (["jpeg", "png", "webp"], {
                    "default": "png"
                }),
                "strength": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate"
    CATEGORY = "Bjornulf"

    def get_next_number(self):
        save_dir = "output/API/Stability"
        os.makedirs(save_dir, exist_ok=True)
        files = [f for f in os.listdir(save_dir) if f.endswith(('.webp', '.png', '.jpeg'))]
        if not files:
            return 1
        numbers = [int(f.split('.')[0]) for f in files]
        return max(numbers) + 1

    def generate(self, api_key, prompt, negative_prompt="", aspect_ratio="1:1", 
                seed=0, output_format="png", strength=1.0):
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "image/*"
        }

        # Prepare the form data
        form_data = {
            "prompt": prompt,
            "output_format": output_format,
            "aspect_ratio": aspect_ratio
        }

        # Add optional parameters if they're provided
        if negative_prompt:
            form_data["negative_prompt"] = negative_prompt
        if seed != 0:
            form_data["seed"] = seed
        if strength != 1.0:
            form_data["strength"] = strength

        # Include a placeholder in the 'files' argument to trigger multipart/form-data
        files = {"placeholder": ("filename", b"")}

        # Make the API request
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/ultra",
            headers=headers,
            files=files,
            data=form_data
        )

        if response.status_code == 200:
            next_num = self.get_next_number()
            filename = f"{next_num:03d}.{output_format}"
            filepath = os.path.join("output/API/Stability", filename)
            
            # Save the image
            with open(filepath, 'wb') as file:
                file.write(response.content)
            
            # Load and process the image for ComfyUI
            img = Image.open(filepath)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Convert to tensor format expected by ComfyUI
            img_tensor = torch.from_numpy(np.array(img).astype(np.float32) / 255.0)
            img_tensor = img_tensor.unsqueeze(0)
            
            return (img_tensor,)
        else:
            raise Exception(str(response.json()))
