import os
import numpy as np
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo

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

        # Determine the next available filename
        counter = 1
        while True:
            filename = f"{output_dir}api_{counter:05d}.png"
            if not os.path.exists(filename):
                break
            counter += 1

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