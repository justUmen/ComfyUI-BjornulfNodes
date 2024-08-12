import random

class TextToStringAndSeed:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"default": 1}),
            },
        }

    RETURN_NAMES = ("text", "random_seed")
    RETURN_TYPES = ("STRING", "INT")
    FUNCTION = "text_with_random_seed"
    CATEGORY = "Bjornulf"

    def text_with_random_seed(self, text, seed):
        # Generate a random seed (integer)
        random_seed = random.randint(0, 2**32 - 1)

        return (text, random_seed)