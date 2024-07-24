import os
import numpy as np
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo

class SaveImageToFolder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", ),
                "folder_name": ("STRING", {"default": "my_folder"}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    FUNCTION = "save_image_to_folder"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def save_image_to_folder(self, images, folder_name, prompt=None, extra_pnginfo=None):
        output_dir = os.path.join("./output", folder_name)
        os.makedirs(output_dir, exist_ok=True)

        results = []
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                for k, v in extra_pnginfo.items():
                    metadata.add_text(k, json.dumps(v))

            counter = 1
            while True:
                filename = os.path.join(output_dir, f"{counter:05d}.png")
                if not os.path.exists(filename):
                    break
                counter += 1

            img.save(filename, format="PNG", pnginfo=metadata)
            print(f"Image saved as: {filename}")
            results.append({"filename": filename})

        return {"ui": {"images": results}}