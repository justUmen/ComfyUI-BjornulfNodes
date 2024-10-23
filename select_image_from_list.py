import torch

class Everything(str):
    def __ne__(self, __value: object) -> bool:
        return False

class SelectImageFromList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "all_images": ("IMAGE", {}),
                "selection": ("INT", {"default": 1, "min": -999999, "max": 999999, "step": 1}),  # Updated to allow negative values
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("selected_image",)
    FUNCTION = "select_an_image"
    CATEGORY = "Bjornulf"

    def select_an_image(self, all_images, selection):
        num_images = all_images.shape[0]
        
        # Convert selection to 0-based index
        if selection > 0:
            index = selection - 1
        else:
            # Handle negative indices directly
            index = selection
        
        # Ensure the index is within bounds
        if index >= num_images:
            index = num_images - 1
        elif index < -num_images:
            index = 0
            
        # Select the image at the specified index
        selected_image = all_images[index].unsqueeze(0)
        
        return (selected_image,)