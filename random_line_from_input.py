import random

class RandomLineFromInput:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"default": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "random_line"
    OUTPUT_IS_LIST = (False,)
    CATEGORY = "Bjornulf"
    
    def random_line(self, text, seed):
        random.seed(seed)
        
        # Split the input text into lines
        lines = text.split('\n')
        
        # Remove empty lines and strip whitespace
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            return ([""],)
        
        # Select a random line
        chosen_line = random.choice(lines)
        
        # Return as a list with one element
        return ([chosen_line],)