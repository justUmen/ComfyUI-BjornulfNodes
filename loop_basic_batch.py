class LoopBasicBatch:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "nb_loops": ("INT", {"default": 1, "min": 0, "max": 1000, "step": 1}),
            },
        }

    RETURN_TYPES = ("INT",)
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "create_loop_basic_batch"
    CATEGORY = "Bjornulf"

    def create_loop_basic_batch(self, nb_loops):
        range_values = list()
        while nb_loops > 0:
            range_values.append(1)
            nb_loops -= 1
        return (range_values,)