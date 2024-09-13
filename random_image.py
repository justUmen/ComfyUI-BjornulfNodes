import random

class RandomImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_of_images": ("INT", {"default": 2, "min": 1, "max": 10, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "random_image"
    CATEGORY = "Bjornulf"

    def random_image(self, number_of_images, **kwargs):
        valid_images = []
        for i in range(1, number_of_images + 1):
            image_key = f"image_{i}"
            if image_key in kwargs and kwargs[image_key] is not None:
                valid_images.append(kwargs[image_key])
        
        if not valid_images:
            raise ValueError("No valid images provided")
        
        random_image = random.choice(valid_images)
        return (random_image,)

    @classmethod
    def IS_CHANGED(cls, number_of_images, ** kwargs):
        return float("nan")  # This will force the node to always update

