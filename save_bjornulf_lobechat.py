import os
import numpy as np
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo
import torch
import gc
import requests

class SaveBjornulfLobeChat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"forceInput": True}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    FUNCTION = "save_bjornulf_lobe_chat"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def save_bjornulf_lobe_chat(self, image, prompt=None, extra_pnginfo=None):
        # First, attempt to free VRAM
        self.free_vram()

        # Ensure the output directory exists
        output_dir = "./output/BJORNULF_LOBECHAT/"
        os.makedirs(output_dir, exist_ok=True)

        # Convert the image from ComfyUI format to PIL Image
        i = 255. * image.cpu().numpy()
        if i.ndim > 3:
            i = np.squeeze(i)
        if i.ndim == 2:
            i = i[:, :, np.newaxis]

        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Find the highest existing file number
        existing_files = [f for f in os.listdir(output_dir) if f.startswith('api_') and f.endswith('.png') and f[4:-4].isdigit()]
        if existing_files:
            highest_num = max(int(f[4:-4]) for f in existing_files)
            counter = highest_num + 1
        else:
            counter = 1

        # Determine the filename
        filename = f"{output_dir}api_{counter:05d}.png"

        # Prepare metadata
        metadata = PngInfo()
        if prompt is not None:
            metadata.add_text("prompt", json.dumps(prompt))
        if extra_pnginfo is not None:
            for k, v in extra_pnginfo.items():
                metadata.add_text(k, json.dumps(v))

        # Update the symbolic link in the output directory
        link_path = "./output/BJORNULF_API_LAST_IMAGE.png"
        if os.path.exists(link_path):
            os.remove(link_path)
        os.symlink(os.path.abspath(filename), link_path)

        # Save the image with the determined filename
        img.save(os.path.abspath(filename), format="PNG", pnginfo=metadata)
        
        print(f"Image saved as: {filename}")

        return {"ui": {"images": [{"filename": filename, "type": "output"}]}}

    def free_vram(self):
        print("Attempting to free VRAM...")
        
        # Clear CUDA cache
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            print("CUDA cache cleared.")
        
        # Run garbage collection
        collected = gc.collect()
        print(f"Garbage collector: collected {collected} objects.")
        
        # Trigger the HTTP request
        self.trigger_http_request()

    def trigger_http_request(self):
        url = "http://localhost:8188/prompt"
        headers = {"Content-Type": "application/json"}
        payload = {
            "prompt": {
                "3": {
                    "inputs": {"text": "free VRAM hack"},
                    "class_type": "Bjornulf_WriteText",
                    "_meta": {"title": "✒ Write Text"}
                },
                "4": {
                    "inputs": {"text_value": ["3", 0], "text": "free VRAM hack"},
                    "class_type": "Bjornulf_ShowText",
                    "_meta": {"title": "👁 Show (Text)"}
                }
            }
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            print("HTTP request triggered successfully")
        except requests.exceptions.RequestException as e:
            print(f"Failed to trigger HTTP request: {e}")