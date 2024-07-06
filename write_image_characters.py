class WriteImageCharacters:
    @classmethod
    def INPUT_TYPES(cls):
        hidden_inputs = {}
        for i in range(2, 6):  # Notice the range starts at 2 and ends at 6 to include 5
            hidden_inputs.update({
                f"character_{i}": ("BJORNULF_CHARACTER", {"forceInput": True}),
                # f"character_{i}": ("STRING", {"forceInput": True}),
            })
        return {
            "required": {
                "number_of_characters": ("INT", {"default": 1, "min": 1, "max": 5, "step": 1}),
                "character_1": ("BJORNULF_CHARACTER", {"forceInput": True}),
                # "character_1": ("STRING", {"forceInput": True}),
            },
            "optional": {
                "other": ("STRING", {"multiline": True, "forceInput": True}),
            },
            "hidden": hidden_inputs
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_image_characters"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def write_image_characters(self, number_of_characters, other="", **kwargs):
        text = f"Other: {other}\n"
        for i in range(1, number_of_characters + 1):
            text += f"{kwargs.get(f'character_{i}', '')}\n"
        return (text,)
