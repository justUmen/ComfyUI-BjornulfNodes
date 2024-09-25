import random
import json
import os
import re

class ScramblerCharacter:
    def __init__(self):
        self.scramble_config = self.load_scramble_config()

    def load_scramble_config(self):
        script_dir = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(script_dir, "scrambler/character_scrambler.json")
        with open(config_path, "r") as f:
            return json.load(f)

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "photography portrait of a happy middle-aged swedish woman nurse with a fit body, wearing a black headband, large blue parka and orange jeans."}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "image_styles": ("BOOLEAN", {"default": False}),
                "ages": ("BOOLEAN", {"default": False}),
                "sex": ("BOOLEAN", {"default": False}),
                "body_types": ("BOOLEAN", {"default": False}),
                "colors": ("BOOLEAN", {"default": False}),
                "emotions": ("BOOLEAN", {"default": False}),
                "nationalities": ("BOOLEAN", {"default": False}),
                "clothing_head": ("BOOLEAN", {"default": False}),
                "clothing_top": ("BOOLEAN", {"default": False}),
                "clothing_bottom": ("BOOLEAN", {"default": False}),
                "occupations": ("BOOLEAN", {"default": False}),
                "sizes": ("BOOLEAN", {"default": False}),
                "image_types": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "scramble_words"
    CATEGORY = "Bjornulf"

    def scramble_words(self, text, seed=None, **kwargs):
        if seed is not None:
            random.seed(seed)

        for category, config in self.scramble_config.items():
            if kwargs.get(f"{category}", config.get("enabled", False)):
                words = config["words"]
                pattern = r'\b(' + '|'.join(re.escape(word) for word in words) + r')\b'
                text = re.sub(pattern, lambda m: random.choice(words), text, flags=re.IGNORECASE)

        return (text,)