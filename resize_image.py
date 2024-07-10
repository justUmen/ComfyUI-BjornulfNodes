import numpy as np
import torch
from PIL import Image

class ResizeImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {}),
                "width": ("INT", {"default": 256}),
                "height": ("INT", {"default": 256}),
            }
        }

    FUNCTION = "resize_image"
    RETURN_TYPES = ("IMAGE",)
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def resize_image(self, image, width=256, height=256):
        # Convert the image from ComfyUI format to PIL Image
        i = 255. * image.cpu().numpy()

        # Reshape the image if it's not in the expected format, remove any leading dimensions of size 1
        if i.ndim > 3:
            i = np.squeeze(i)
        # Ensure the image is 3D (height, width, channels)
        if i.ndim == 2:
            i = i[:, :, np.newaxis]  # Add a channel dimension if it's missing

        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        # Resize the image
        img_resized = img.resize((width, height), Image.LANCZOS)

        # Convert the PIL image back to numpy array
        img_resized_np = np.array(img_resized).astype(np.float32) / 255.0

        # Assuming ComfyUI format needs the image back in tensor format, convert it back
        img_resized_tensor = torch.tensor(img_resized_np)

        return (img_resized_tensor, )
