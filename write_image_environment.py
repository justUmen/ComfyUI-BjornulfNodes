class WriteImageEnvironment:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "art_style": (["drawing", "digital art", "photography"],),
                "location": ("STRING", {"multiline": True}),
                "lighting": ("STRING", {"multiline": True}),
                "camera_angle": ("STRING", {"multiline": True}),
            },
            "optional": {
                "other": ("STRING", {"multiline": True, "forceInput": True},),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_image_environment"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def write_image_environment(self, art_style, location, lighting, camera_angle, **kwargs):
        text = f"Art Style: {art_style}\n\n"
        text += f"Location:\n{location}\n\n"
        text += f"Lighting:\n{lighting}\n\n"
        text += f"Camera Angle:\n{camera_angle}\n\n"
        return (text,)