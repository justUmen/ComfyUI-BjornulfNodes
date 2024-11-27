import numpy as np
import torch
from PIL import Image

class ResizeImagePercentage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {}),
                "percentage": ("INT", {
                    "default": 50,
                    "min": 1,
                    "max": 1000,
                    "step": 1,
                }),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    FUNCTION = "resize_image"
    RETURN_TYPES = ("IMAGE", "INT", "INT",)
    RETURN_NAMES = ("IMAGE", "width", "height")
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def resize_image(self, image, percentage=100.0, prompt=None, extra_pnginfo=None):
        # Convert percentage to decimal (e.g., 150% -> 1.5)
        scale_factor = percentage / 100.0
        
        # Ensure the input image is on CPU and convert to numpy array
        image_np = image.cpu().numpy()
        
        # Initialize new_width and new_height
        new_width = 0
        new_height = 0
        
        # Check if the image is in the format [batch, height, width, channel]
        if image_np.ndim == 4:
            # Process each image in the batch
            resized_images = []
            for img in image_np:
                # Get original dimensions
                orig_height, orig_width = img.shape[:2]
                
                # Calculate new dimensions
                new_width = int(orig_width * scale_factor)
                new_height = int(orig_height * scale_factor)
                
                # Convert to PIL Image
                pil_img = Image.fromarray((img * 255).astype(np.uint8))
                # Resize
                resized_pil = pil_img.resize((new_width, new_height), Image.LANCZOS)
                # Convert back to numpy and normalize
                resized_np = np.array(resized_pil).astype(np.float32) / 255.0
                resized_images.append(resized_np)
            
            # Stack the resized images back into a batch
            resized_batch = np.stack(resized_images)
            # Convert to torch tensor
            resized_tensor = torch.from_numpy(resized_batch)
        else:
            # If it's a single image, process it directly
            # Get original dimensions
            orig_height, orig_width = image_np.shape[:2]
            
            # Calculate new dimensions
            new_width = int(orig_width * scale_factor)
            new_height = int(orig_height * scale_factor)
            
            # Convert to PIL Image
            pil_img = Image.fromarray((image_np * 255).astype(np.uint8))
            # Resize
            resized_pil = pil_img.resize((new_width, new_height), Image.LANCZOS)
            # Convert back to numpy and normalize
            resized_np = np.array(resized_pil).astype(np.float32) / 255.0
            # Add batch dimension if it was originally present
            if image.dim() == 4:
                resized_np = np.expand_dims(resized_np, axis=0)
            # Convert to torch tensor
            resized_tensor = torch.from_numpy(resized_np)

        # Update metadata if needed
        if extra_pnginfo is not None:
            extra_pnginfo["resize_percentage"] = percentage
            extra_pnginfo["resized_width"] = new_width
            extra_pnginfo["resized_height"] = new_height

        return (resized_tensor, new_width, new_height)