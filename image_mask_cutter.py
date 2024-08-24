import torch

class ImageMaskCutter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "cut_image"

    CATEGORY = "Bjornulf"

    def cut_image(self, image, mask):
        print(f"Image shape: {image.shape}")
        print(f"Mask shape: {mask.shape}")

        # Check if image channels are in the last dimension
        if image.shape[-1] == 3 or image.shape[-1] == 4:
            # Move channels to second dimension
            image = image.permute(0, 3, 1, 2)

        # Ensure image and mask have compatible dimensions
        if image.shape[2:] != mask.shape[1:]:
            raise ValueError(f"Image and mask must have compatible dimensions. Got image shape {image.shape} and mask shape {mask.shape}")

        # Convert mask to float and ensure it's in the range [0, 1]
        mask = mask.float()
        mask = torch.clamp(mask, 0, 1)

        # If image is RGB, convert to RGBA
        if image.shape[1] == 3:
            alpha = torch.ones((image.shape[0], 1, image.shape[2], image.shape[3]), device=image.device)
            image = torch.cat([image, alpha], dim=1)

        # Use the mask as the alpha channel
        image[:, 3:4, :, :] = mask.unsqueeze(1)

        # Move channels back to the last dimension
        cut_image = image.permute(0, 2, 3, 1)

        return (cut_image,)