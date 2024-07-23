import ollama
from ollama import Client  # pip install ollama

class ollamaLoader:
    @classmethod
    def get_available_models(cls):
        try:
            list_models = ollama.list()
            return [model['name'] for model in list_models['models']]
        except Exception as e:
            print(f"Error fetching models: {e}")
            return ["dolphin-llama3"]  # Return a default model if fetching fails

    @classmethod
    def INPUT_TYPES(cls):
        default_system_prompt = "Describe a specific example of an object, animal, person, or landscape based on a given general idea. Start with a clear and concise overall description in the first sentence. Then, provide a detailed depiction of its physical features, focusing on colors, size, clothing, eyes, and other distinguishing characteristics. Use commas to separate each detail and avoid listing them. Ensure each description is vivid, precise, and specific to one unique instance of the subject. Refrain from using poetic language and giving it a name.\nExample input: man\n Example output: \nAn overweight old man sitting on a bench, wearing a blue hat, yellow pants, orange jacket and black shirt, sunglasses, very long beard, very pale skin, long white hair, very large nose."
        return {
            "required": {
                "user_prompt": ("STRING", {"multiline": True}),
                "selected_model": (cls.get_available_models(),),
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": default_system_prompt
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ollama_response",)
    FUNCTION = "connect_2_ollama"
    CATEGORY = "Bjornulf"

    def connect_2_ollama(self, user_prompt, selected_model, system_prompt):
        keep_alive = 0
        client = Client(host="http://127.0.0.1:11434")
        response = client.generate(
            model=selected_model,
            system=system_prompt,
            prompt=user_prompt,
            keep_alive=str(keep_alive) + "m"
        )
        print("Ollama response : ", response['response'])
        return (response['response'],)