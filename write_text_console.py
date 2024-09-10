import logging
class WriteTextInConsole:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            }
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_text_in_console"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (False,)
    CATEGORY = "Bjornulf"
    
    def write_text_in_console(self, text):
        logging.info(f"Text: {text}")
        return {"ui": {"text": text}, "result": (text,)}
