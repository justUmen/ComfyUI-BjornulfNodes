import os

class SaveText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "forceInput": True}),
                "filename": ("STRING", {"default": "001.txt"})
            }
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "save_text"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"
    # OUTPUT_IS_LIST = (True,)
    
    def save_text(self, text, filename):
        directory = "custom_nodes/Bjornulf_custom_nodes/SaveText/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = os.path.join(directory, filename)

        while os.path.exists(new_filename):
            new_filename = os.path.join(directory, f"{base}_{counter:03d}{ext}")
            counter += 1

        with open(new_filename, 'w') as file:
            file.write(text)
        
        return {"ui": {"text": text}, "result": (text,)}