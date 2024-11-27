class ShowInt:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "INT": ("INT", {"default": 0, "forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "show_int"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def detect_type(self, value):
        return 'integer'

    def show_int(self, INT):
        type_info = [f"{value}" for value in INT]
        return {"ui": {"text": type_info}}

class ShowFloat:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "FLOAT": ("FLOAT", {"default": 0.0, "forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "show_float"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def detect_type(self, value):
        return 'float'

    def show_float(self, FLOAT):
        type_info = [f"{value}" for value in FLOAT]
        return {"ui": {"text": type_info}}


class ShowStringText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "STRING": ("STRING", {"default": "", "forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "show_string"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def detect_type(self, value):
        if isinstance(value, int):
            return 'integer'
        elif isinstance(value, float):
            # Check if it has a decimal part
            if value % 1 == 0:
                return 'float' if str(value).endswith('.0') else 'integer'
            return 'float'
        elif isinstance(value, str):
            try:
                float_val = float(value)
                if '.' in value:
                    return 'float string'
                if float_val.is_integer():
                    return 'integer string'
                return 'float string'
            except ValueError:
                return 'normal string'
        else:
            return 'other type'

    def show_string(self, STRING):
        type_info = [f"{value}" for value in STRING]
        return {"ui": {"text": type_info}}

class ShowJson:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "STRING": ("STRING", {"default": "", "forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "show_json"
    OUTPUT_NODE = True
    INPUT_IS_LIST = (True,)
    CATEGORY = "Bjornulf"
    
    def detect_type(self, value):
        if isinstance(value, int):
            return 'integer'
        elif isinstance(value, float):
            if value % 1 == 0:
                return 'float' if str(value).endswith('.0') else 'integer'
            return 'float'
        elif isinstance(value, str):
            try:
                float_val = float(value)
                if '.' in value:
                    return 'float string'
                if float_val.is_integer():
                    return 'integer string'
                return 'float string'
            except ValueError:
                return 'normal string'
        else:
            return 'other type'

    def show_json(self, STRING):
        import json
        try:
            # Join all characters into a single string
            full_string = "".join(STRING)
            try:
                # Parse JSON
                parsed_json = json.loads(full_string)
                # Format JSON with proper indentation and Unicode support
                formatted_json = json.dumps(
                    parsed_json,
                    indent=2,  # You can adjust this number for different indentation levels
                    ensure_ascii=False,
                    sort_keys=True  # Optional: sorts keys alphabetically
                )
                # Add newlines for better readability
                formatted_json = f"\n{formatted_json}\n"
                # Return as a single-element list
                return {"ui": {"text": [formatted_json]}}
            except json.JSONDecodeError as e:
                # If not valid JSON, return error message
                return {"ui": {"text": [f"Invalid JSON: {str(e)}\nOriginal string:\n{full_string}"]}}
        except Exception as e:
            return {"ui": {"text": [f"Error processing string: {str(e)}"]}}