
class Everything(str):
    def __ne__(self, __value: object) -> bool:
        return False

class TextToAnything:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { "text": ("STRING",{"forceInput":True}) },
        }

    @classmethod
    def VALIDATE_INPUTS(s, input_types):
        return True
    
    RETURN_TYPES = (Everything("*"),)
    RETURN_NAMES = ("anything",)
    FUNCTION = "text_to_any"
    CATEGORY = "Bjornulf"
    
    def text_to_any(self, text):
        return (text,)