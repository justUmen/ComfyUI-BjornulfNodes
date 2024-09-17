class Everything(str):
    def __ne__(self, __value: object) -> bool:
        return False

class IfElse:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("STRING", {"forceInput": True, "multiline": False}),
                "send_if_true": (Everything("*"),),
                "send_if_false": (Everything("*"),),
                "compare_with": ("STRING", {"multiline": False}),
            },
        }

    RETURN_TYPES = (Everything("*"),"STRING")
    RETURN_NAMES = ("output","true_or_false")
    FUNCTION = "if_else"
    CATEGORY = "Bjornulf"

    def if_else(self, input, send_if_true, send_if_false, compare_with):
        if input == compare_with:
            return (send_if_true,"True")
        else:
            return (send_if_false,"False")