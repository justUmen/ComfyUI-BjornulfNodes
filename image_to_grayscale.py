import torch

class GrayscaleTransform:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "preserve_alpha": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "transform_to_grayscale"

    CATEGORY = "Bjornulf"

    def transform_to_grayscale(self, image, preserve_alpha):
        # Check if the image has an alpha channel
        has_alpha = image.shape[3] == 4

        # Extract RGB channels
        rgb = image[:, :, :, :3]

        # Convert to grayscale using the luminosity method
        # Weights are based on human perception of color
        grayscale = 0.2989 * rgb[:,:,:,0] + 0.5870 * rgb[:,:,:,1] + 0.1140 * rgb[:,:,:,2]
        
        # Expand dimensions to match original shape
        grayscale = grayscale.unsqueeze(-1).repeat(1, 1, 1, 3)

        if has_alpha and preserve_alpha:
            # If the original image had an alpha channel and we want to preserve it
            alpha = image[:, :, :, 3:4]
            result = torch.cat([grayscale, alpha], dim=3)
        else:
            result = grayscale

        return (result,)