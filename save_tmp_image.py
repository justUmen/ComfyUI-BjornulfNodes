import os
import numpy as np
from PIL import Image

class SaveTmpImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {"forceInput": True}),
            }
        }

    FUNCTION = "save_image"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def save_image(self, image):
        # Ensure the output directory exists
        # os.makedirs("./output", exist_ok=True)

        # Convert the image from ComfyUI format to PIL Image
        # Assuming the first two dimensions are extra, and we need to keep the last two
        i = 255. * image.cpu().numpy()
        # Reshape the image if it's not in the expected format, remove any leading dimensions of size 1
        if i.ndim > 3:
            i = np.squeeze(i)
        # Ensure the image is 3D (height, width, channels)
        if i.ndim == 2:
            i = i[:, :, np.newaxis]  # Add a channel dimension if it's missing

        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Save the image, overwriting if it exists
        img.save("./output/tmp_api.png", format="PNG")

        return ()
