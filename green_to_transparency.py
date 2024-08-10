import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms

class GreenScreenToTransparency:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE", {}),
                "threshold": ("FLOAT", {"default": 0.1, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    FUNCTION = "remove_green_screen"
    RETURN_TYPES = ("IMAGE",)
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def remove_green_screen(self, image, threshold=0.1, prompt=None, extra_pnginfo=None):
        # Ensure the input image is on CPU and convert to numpy array
        image_np = image.cpu().numpy()
        
        # Check if the image is in the format [batch, height, width, channel]
        if image_np.ndim == 4:
            # If so, we'll process each image in the batch
            processed_images = []
            for img in image_np:
                processed_img = self._process_single_image(img, threshold)
                processed_images.append(processed_img)
            
            # Stack the processed images back into a batch
            processed_batch = np.stack(processed_images)
            # Convert to torch tensor
            processed_tensor = torch.from_numpy(processed_batch)
        else:
            # If it's a single image, process it directly
            processed_np = self._process_single_image(image_np, threshold)
            # Add batch dimension if it was originally present
            if image.dim() == 4:
                processed_np = np.expand_dims(processed_np, axis=0)
            # Convert to torch tensor
            processed_tensor = torch.from_numpy(processed_np)

        # Update metadata if needed
        if extra_pnginfo is not None:
            extra_pnginfo["green_screen_removed"] = True

        return (processed_tensor, prompt, extra_pnginfo)

    def _process_single_image(self, img, threshold):
        # Convert to PIL Image
        pil_img = Image.fromarray((img * 255).astype(np.uint8))
        
        # Convert the image to RGBA mode
        pil_img = pil_img.convert("RGBA")
        
        # Get image data as numpy array
        data = np.array(pil_img)
        
        # Create a mask for green pixels
        r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
        mask = (g > r + threshold * 255) & (g > b + threshold * 255)
        
        # Set alpha channel to 0 for green pixels
        data[:,:,3] = np.where(mask, 0, a)
        
        # Create a new image with the updated data
        result = Image.fromarray(data)
        
        # Convert back to numpy and normalize
        processed_np = np.array(result).astype(np.float32) / 255.0
        
        return processed_np