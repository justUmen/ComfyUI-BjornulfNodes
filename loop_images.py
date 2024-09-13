class LoopImages:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_of_images": ("INT", {"default": 2, "min": 1, "max": 10, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "loop_images"
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"

    def loop_images(self, number_of_images, **kwargs):
        image_list = []
        for i in range(1, number_of_images + 1):
            image_key = f"image_{i}"
            if image_key in kwargs and kwargs[image_key] is not None:
                image_list.append(kwargs[image_key])
        return (image_list,)

    @classmethod
    def IS_CHANGED(cls, number_of_images, ** kwargs):
        return float("nan")  # This will force the node to always update

