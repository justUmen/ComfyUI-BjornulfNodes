import re
import random
import time

class WriteText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
            "hidden": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "control_after_update": ("INT", {"default": 0})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_text"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"
    
    def write_text(self, text, seed=None, control_after_update=None):
        # If seed is not provided, generate a new one
        if seed is None:
            seed = int(time.time() * 1000)
        
        # Use the seed to initialize the random number generator
        random.seed(seed)
        
        def replace_random(match):
            options = match.group(1).split('|')
            return random.choice(options)

        pattern = r'\{([^}]+)\}'
        result = re.sub(pattern, replace_random, text)
        
        return (result,)

    @classmethod
    def IS_CHANGED(s, text, seed=None, control_after_update=None):
        # This method is called to determine if the node needs to be re-executed
        return float("nan")  # Always re-execute to ensure consistency