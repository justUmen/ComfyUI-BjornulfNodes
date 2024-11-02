class ShowInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_value": ("INT", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "show_int"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def show_int(self, int_value):
        return {"ui": {"text": int_value}}
