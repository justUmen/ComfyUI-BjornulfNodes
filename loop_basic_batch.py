class Everything(str):
    def __ne__(self, __value: object) -> bool:
        return False

class LoopBasicBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "nb_loops": ("INT", {"default": 1, "min": 0, "max": 1000, "step": 1}),
                "default_text": ("STRING", {"default": "Default input"})
            },
            "optional": {
                "input": (Everything("*"),)
            },
        }

    RETURN_TYPES = (Everything("*"),)
    RETURN_NAMES = ("output",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "create_loop_basic_batch"
    CATEGORY = "Bjornulf"

    def create_loop_basic_batch(self, nb_loops, default_text, input=None):
        if input is not None:
            return ([input] * nb_loops,)
        
        # Determine the type of the default_text
        if default_text.isdigit():
            self.RETURN_TYPES = ("INT",)
            output = int(default_text)
        elif default_text.replace('.', '', 1).isdigit() and default_text.count('.') == 1:
            self.RETURN_TYPES = ("FLOAT",)
            output = float(default_text)
        else:
            self.RETURN_TYPES = ("STRING",)
            output = default_text

        return ([output] * nb_loops,)