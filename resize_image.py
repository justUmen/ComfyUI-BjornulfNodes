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
        # Ensure the input image is on CPU and convert to numpy array
        image_np = image.cpu().numpy()
        
        # Check if the image is in the format [batch, height, width, channel]
        if image_np.ndim == 4:
            # If so, we'll process each image in the batch
            resized_images = []
            for img in image_np:
                # Convert to PIL Image
                pil_img = Image.fromarray((img * 255).astype(np.uint8))
                # Resize
                resized_pil = pil_img.resize((width, height), Image.LANCZOS)
                # Convert back to numpy and normalize
                resized_np = np.array(resized_pil).astype(np.float32) / 255.0
                resized_images.append(resized_np)
            
            # Stack the resized images back into a batch
            resized_batch = np.stack(resized_images)
            # Convert to torch tensor
            return (torch.from_numpy(resized_batch),)
        else:
            # If it's a single image, process it directly
            # Convert to PIL Image
            pil_img = Image.fromarray((image_np * 255).astype(np.uint8))
            # Resize
            resized_pil = pil_img.resize((width, height), Image.LANCZOS)
            # Convert back to numpy and normalize
            resized_np = np.array(resized_pil).astype(np.float32) / 255.0
            # Add batch dimension if it was originally present
            if image.dim() == 4:
                resized_np = np.expand_dims(resized_np, axis=0)
            # Convert to torch tensor
            return (torch.from_numpy(resized_np),)