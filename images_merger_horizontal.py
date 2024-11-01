import torch
import numpy as np
from PIL import Image

class MergeImagesHorizontally:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
            },
            "optional": {
                "image3": ("IMAGE",),
                "image4": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "combine_images"

    CATEGORY = "Bjornulf"

    def combine_images(self, image1, image2, image3=None, image4=None):
        # Collect all provided images
        images = [image1, image2]
        if image3 is not None:
            images.append(image3)
        if image4 is not None:
            images.append(image4)
        
        # Calculate the total width and maximum height
        total_width = sum(img.shape[2] for img in images)  # Sum of widths
        max_height = max(img.shape[1] for img in images)   # Maximum height
        
        # Create a new tensor for the combined image
        combined_image = torch.zeros((images[0].shape[0], max_height, total_width, 3), dtype=images[0].dtype, device=images[0].device)
        
        # Paste images side by side
        current_x = 0
        for img in images:
            b, h, w, c = img.shape
            combined_image[:, :h, current_x:current_x+w, :] = img
            
            # Blend the edge pixels if it's not the last image
            # if current_x + w < total_width:
            #     combined_image[:, :h, current_x+w-1:current_x+w+1, :] = torch.mean(
            #         torch.stack([
            #             combined_image[:, :h, current_x+w-1:current_x+w, :],
            #             combined_image[:, :h, current_x+w:current_x+w+1, :]
            #         ]), dim=0
            #     )
            
            current_x += w
        
        return (combined_image,)
