import os

class SaveText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "forceInput": True}),
                "filepath": ("STRING", {"default": "output/this_test.txt"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "save_text"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"
    
    def save_text(self, text, filepath):
        # Validate file extension
        if not filepath.lower().endswith('.txt'):
            raise ValueError("Output file must be a .txt file")
            
        try:
            # Create directory if it doesn't exist
            directory = os.path.dirname(filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            # Append text to file with a newline
            with open(filepath, 'a', encoding='utf-8') as file:
                file.write(text + '\n')
            
            return {"ui": {"text": text}, "result": (text,)}
            
        except (OSError, IOError) as e:
            raise ValueError(f"Error saving file: {str(e)}")