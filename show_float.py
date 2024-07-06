class ShowFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_value": ("FLOAT", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "show_float"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def show_float(self, float_value):
        return {"ui": {"text": float_value}}
