class ShowText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_value": ("STRING", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "show_text"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def show_text(self, text_value):
        return {"ui": {"text": text_value}}
