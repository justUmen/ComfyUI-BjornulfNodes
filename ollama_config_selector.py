class OllamaConfig:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ollama_url": ("STRING", {"default": "http://0.0.0.0:11434"}),
                "model_name": ("STRING", {"default": "undefined"})  # Empty list with no default
            }
        }

    RETURN_TYPES = ("OLLAMA_CONFIG",)
    RETURN_NAMES = ("OLLAMA_CONFIG",)
    FUNCTION = "select_model"
    CATEGORY = "ollama"

    def select_model(self, ollama_url, model_name):
        return ({"model": model_name, "url": ollama_url},)

    @classmethod
    def IS_CHANGED(cls, ollama_url, model_name) -> float:
        return 0.0