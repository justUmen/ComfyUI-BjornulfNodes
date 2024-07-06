import random

class RandomTexts:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_of_inputs": ("INT", {"default": 2, "min": 2, "max": 30, "step": 1}),
                "number_of_random": ("INT", {"default": 1, "min": 1, "max": 30, "step": 1}),
                "text_1": ("STRING", {"forceInput": "True"}),
                "text_2": ("STRING", {"forceInput": "True"}),
                "seed": ("INT", {"default": "1"}), #Used with control_after_generate,
            },
            "hidden": {
                **{f"text_{i}": ("STRING", {"forceInput": "True"}) for i in range(3, 31)}
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "random_texts"
    OUTPUT_IS_LIST = (False,)
    CATEGORY = "Bjornulf"
    
    def random_texts(self, number_of_inputs, number_of_random, **kwargs):
        texts = [kwargs[f"text_{i}"] for i in range(1, number_of_inputs + 1) if f"text_{i}" in kwargs]
        random_texts = random.sample(texts, min(number_of_random, len(texts)))
        return (random_texts,)