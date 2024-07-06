class WriteImageAllInOne:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "art_style": (["none", "drawing", "digital art", "photography"],),
                "location": ("STRING", {"forceInput": "True"}),
                "lighting": ("STRING", {"multiline": True}),
                "camera_angle": ("STRING", {"multiline": True}),
            },
            "optional": {
                "other": ("STRING", {"multiline": True},),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "write_image_allinone"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def write_image_allinone(self, art_style, location, lighting, camera_angle, other=""):
        text = f"Art Style: {art_style}\n\n"
        text += f"Location:\n{location}\n\n"
        text += f"Lighting:\n{lighting}\n\n"
        text += f"Camera Angle:\n{camera_angle}\n\n"
        if other:
            text += f"Other:\n{other}\n\n"
        return (text,)

    @classmethod
    def CREATE_CONNECTED_NODES(cls):
        return [
            {
                "class_type": "PrimitiveNode",
                "inputs": {
                    "value": "drawing",
                    "label": "Art Style",
                    "type": "combo",
                    "options": ["drawing", "digital art", "photography"]
                },
                "output": ["art_style"]
            },
            {
                "class_type": "PrimitiveNode",
                "inputs": {
                    "value": "",
                    "label": "Location",
                    "type": "text",
                    "multiline": True
                },
                "output": ["location"]
            },
            {
                "class_type": "PrimitiveNode",
                "inputs": {
                    "value": "",
                    "label": "Lighting",
                    "type": "text",
                    "multiline": True
                },
                "output": ["lighting"]
                },
            {
                "class_type": "PrimitiveNode",
                "inputs": {
                    "value": "",
                    "label": "Camera Angle",
                    "type": "text",
                    "multiline": True
                },
                "output": ["camera_angle"]
            },
            {
                "class_type": "PrimitiveNode",
                "inputs": {
                    "value": "",
                    "label": "Other",
                    "type": "text",
                    "multiline": True
                },
                "output": ["other"]
            }
        ]