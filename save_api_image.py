import os
import numpy as np
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo

class SaveApiImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"forceInput": True}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    FUNCTION = "save_api_image"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def save_api_image(self, image, prompt=None, extra_pnginfo=None):
        # Ensure the output directory exists
        os.makedirs("./output/", exist_ok=True)

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
            filename = f"./output/api_{counter:05d}.png"
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

        # Save the image with the determined filename and metadata
        img.save(filename, format="PNG", pnginfo=metadata)

        # Write the number of the last image to a text file with leading zeroes
        with open("./output/api_next_image.txt", "w") as f:
            f.write(f"api_{counter+1:05d}.png")

        print(f"Image saved as: {filename}")

        return {"ui": {"images": [{"filename": filename, "type": "output"}]}}