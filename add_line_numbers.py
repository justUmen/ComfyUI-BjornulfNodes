class AddLineNumbers:
    def __init__(self):
        self.font_size = 14
        self.padding = 10
        self.line_height = self.font_size + 4
        self.gutter_width = 50  # Width for line numbers
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "add_line_numbers"
    CATEGORY = "Bjornulf"

    def add_line_numbers(self, text):
        lines = text.split('\n')
        
        # Add line numbers
        numbered_lines = []
        for i, line in enumerate(lines, 1):
            numbered_lines.append(f"{i:4d} | {line}")
        # Join back into a single string
        result = '\n'.join(numbered_lines)
        
        return (result,)