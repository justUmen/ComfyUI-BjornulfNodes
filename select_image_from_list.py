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
                "selection": ("INT", {"default": 1, "min": 1, "max": 999, "step": 1}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("selected_image",)
    FUNCTION = "select_an_image"
    CATEGORY = "Bjornulf"

    def select_an_image(self, all_images, selection):
        # Ensure the selection is within bounds
        selection = max(1, min(selection, all_images.shape[0]))
        
        # Adjust selection to 0-based index
        index = selection - 1
        
        # Select the image at the specified index
        selected_image = all_images[index].unsqueeze(0)
        
        return (selected_image,)