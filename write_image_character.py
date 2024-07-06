class WriteImageCharacter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "description": ("STRING", {"multiline": True}),
                "action": ("STRING", {"multiline": False}),
                "emotion": ("STRING", {"multiline": False}),
                "clothes": ("STRING", {"multiline": False}),
            },
        }

    # RETURN_TYPES = ("STRING",)
    RETURN_TYPES = ("BJORNULF_CHARACTER",)
    RETURN_NAMES = ("character_details",)
    FUNCTION = "write_image_character"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def write_image_character(self, description, action, emotion, clothes):
        text = f"{description}, {action}, {emotion}, {clothes}"
        return (text,)