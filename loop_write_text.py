import re
import itertools

class LoopWriteText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("texts",)
    FUNCTION = "loop_write_text"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def loop_write_text(self, text):
        pattern = r'\{([^}]+)\}'
        matches = re.findall(pattern, text)
        
        if not matches:
            return ([text],)
        
        options_list = [opt.split('|') for opt in matches]
        combinations = list(itertools.product(*options_list))
        
        results = []
        for combo in combinations:
            result = text
            for i, match in enumerate(matches):
                result = result.replace(f"{{{match}}}", combo[i], 1)
            results.append(result)
        
        return (results,)

    @classmethod
    def IS_CHANGED(s, text):
        return float("nan")  # Always re-execute to ensure consistency