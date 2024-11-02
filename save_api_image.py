import os
import numpy as np
from PIL import Image

class SaveApiImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"forceInput": True}),
            }
        }

    FUNCTION = "save_api_image"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def save_api_image(self, image):
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

        # Save the image with the determined filename
        img.save(filename, format="PNG")

        # Write the number of the last image to a text file with leading zeroes
        with open("./output/api_next_image.txt", "w") as f:
            f.write(f"api_{counter+1:05d}.png")

        return ()
