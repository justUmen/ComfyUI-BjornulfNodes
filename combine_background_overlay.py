import torch
import numpy as np
from PIL import Image

class CombineBackgroundOverlay:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "background": ("IMAGE",),
                "overlay_alpha": ("IMAGE",),
                "position": (["middle", "top", "bottom"],),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "combine_background_overlay"
    CATEGORY = "Bjornulf"

    def combine_background_overlay(self, background, overlay_alpha, position):
        # Convert background from torch tensor to numpy array
        bg = background[0].numpy()
        bg = (bg * 255).astype(np.uint8)
        bg_img = Image.fromarray(bg, 'RGB')

        results = []

        for overlay in overlay_alpha:
            # Convert overlay from torch tensor to numpy array
            ov = overlay.numpy()
            ov = (ov * 255).astype(np.uint8)

            # Create PIL Image for overlay
            if ov.shape[2] == 4:
                ov_img = Image.fromarray(ov, 'RGBA')
            else:
                ov_img = Image.fromarray(ov, 'RGB')
                ov_img = ov_img.convert('RGBA')

            # Calculate position based on user selection
            x = (bg_img.width - ov_img.width) // 2
            if position == "middle":
                y = (bg_img.height - ov_img.height) // 2
            elif position == "top":
                y = 0
            else:  # bottom
                y = bg_img.height - ov_img.height

            # Create a new image for this overlay
            result = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))

            # Paste the background
            result.paste(bg_img, (0, 0))

            # Paste the overlay in the selected position
            result.paste(ov_img, (x, y), ov_img)

            # Convert back to numpy array and then to torch tensor
            result_np = np.array(result)
            
            # If the result is RGBA, convert to RGB
            if result_np.shape[2] == 4:
                result_np = result_np[:,:,:3]

            result_tensor = torch.from_numpy(result_np).float() / 255.0

            results.append(result_tensor)

        # Stack all results into a single tensor
        final_result = torch.stack(results)

        return (final_result,)