class LoopAllLines:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "all_lines"
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def all_lines(self, text):
        # Split the input text into lines
        lines = text.split('\n')
        
        # Remove empty lines and strip whitespace
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            return ([],)
        
        # Return all non-empty lines
        return (lines,)