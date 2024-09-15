import re
import random
import time
import logging

class WriteTextAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "lines": 10}),
            },
            "optional": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_text_special"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"
    
    def write_text_special(self, text, seed=None):
        logging.info(f"Raw text: {text}")
        # If seed is not provided, generate a new one
        if len(text) > 10000:
            return ("Text too large to process at once. Please split into smaller parts.",)
        
        if seed is None or seed == 0:
            seed = int(time.time() * 1000)
        
        random.seed(seed)
        
        pattern = r'\{([^}]+)\}'
        
        def replace_random(match):
            return random.choice(match.group(1).split('|'))

        result = re.sub(pattern, replace_random, text)
        logging.info(f"Picked text: {result}")
        
        return (result,)

    @classmethod
    def IS_CHANGED(s, text, seed=None):
        return (text, seed)

