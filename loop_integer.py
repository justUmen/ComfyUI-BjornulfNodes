# class AnyType(str):
#     def __ne__(self, __value: object) -> bool:
#         return False
# any_type = AnyType("*")

class LoopInteger:
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "from_this": ("INT", {"default": 0, "min": 0, "max": 1000, "step": 1}),
                "to_that": ("INT", {"default": 10, "min": 0, "max": 1000, "step": 1}),
                "jump": ("INT", {"default": 1, "min": 0, "max": 1000, "step": 1}),
            },
            # "optional": {
            #     "nb_loops": (any_type,)
            # }
        }

    RETURN_TYPES = ("INT",)
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "create_loop_integer"
    CATEGORY = "Bjornulf"

    def create_loop_integer(self, from_this, to_that, jump):
        range_values = list()
        current_value = from_this
        while current_value <= to_that:
            range_values.append(current_value)
            current_value += jump
        return (range_values,)