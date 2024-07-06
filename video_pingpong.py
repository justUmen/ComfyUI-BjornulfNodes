import torch

class VideoPingPong:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "pingpong_images"
    CATEGORY = "Bjornulf"

    def pingpong_images(self, images):
        if isinstance(images, torch.Tensor):
            reversed_images = torch.flip(images, [0])
            combined_images = torch.cat((images, reversed_images[1:]), dim=0)
        else:
            reversed_images = images[::-1]
            combined_images = images + reversed_images[1:]
        return (combined_images,)