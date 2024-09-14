class LoopTexts:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_of_inputs": ("INT", {"default": 2, "min": 2, "max": 50, "step": 1}),
                # "text_1": ("STRING", {"forceInput": "True"}),
                # "text_2": ("STRING", {"forceInput": "True"}),
            },
            "hidden": {
                **{f"text_{i}": ("STRING", {"forceInput": "True"}) for i in range(1, 51)}
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "loop_texts"
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"

    def loop_texts(self, number_of_inputs, **kwargs):
        text_list = [kwargs[f"text_{i}"] for i in range(1, number_of_inputs + 1) if f"text_{i}" in kwargs]
        return (text_list,)
