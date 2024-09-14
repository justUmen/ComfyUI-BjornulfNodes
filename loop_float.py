from decimal import Decimal, ROUND_HALF_UP
class LoopFloat:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "from_this": ("FLOAT", {"default": 0.00, "min": 0.00, "max": 1000.00, "step": 0.01}),
                "to_that": ("FLOAT", {"default": 10.00, "min": 0.00, "max": 1000.00, "step": 0.01}),
                "jump": ("FLOAT", {"default": 1.00, "min": 0.00, "max": 1000.00, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "create_loop_float"
    CATEGORY = "Bjornulf"

    def create_loop_float(self, from_this, to_that, jump):
        range_values = []
        current_value = Decimal(str(from_this))
        to_that = Decimal(str(to_that))
        jump = Decimal(str(jump))
        
        while current_value <= to_that:
            range_values.append(float(current_value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
            current_value += jump
        
        return (range_values,)