import torch

class RemoveTransparency:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "recover_background": ("BOOLEAN", {"default": False}),
                "background_color": (["black", "white", "greenscreen"], {"default": "black"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_transparency"

    CATEGORY = "Bjornulf"

    def process_transparency(self, image, recover_background, background_color):
        # Check if the image has an alpha channel
        if image.shape[3] == 4:
            rgb = image[:, :, :, :3]
            alpha = image[:, :, :, 3:4]
            
            if recover_background:
                result = rgb
            else:
                # Create background color tensor
                if background_color == "white":
                    bg_color = torch.ones_like(rgb)
                elif background_color == "greenscreen":
                    bg_color = torch.zeros_like(rgb)
                    bg_color[:, :, :, 1] = 1  # Set green channel to 1
                else:  # black
                    bg_color = torch.zeros_like(rgb)
                
                # Blend the image with the background color
                result = rgb * alpha + bg_color * (1 - alpha)
        else:
            # If there's no alpha channel, return the original image
            result = image

        # Ensure the output is always 3 channels (RGB)
        if result.shape[3] == 4:
            result = result[:, :, :, :3]

        return (result,)