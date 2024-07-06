import ollama
from ollama import Client  # pip install ollama

class ollamaLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_prompt": ("STRING", {"multiline": True}),
                # "selected_model": ((), {}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ollama_response",)
    FUNCTION = "connect_2_ollama"
    # INPUT_NODE = True  # Changed from OUTPUT_NODE to INPUT_NODE
    CATEGORY = "Bjornulf"

    # @classmethod
    def connect_2_ollama(self, user_prompt):
        keep_alive = 0
        list_models=ollama.list() #{'models': [{'name': 'dolphin-llama3:latest', 'model': 'dolphin-llama3:latest', 'modified_at': '2024-04-24T06:56:57.498527412+02:00', 'size': 4661235994, 'digest': '613f068e29f863bb900e568f920401b42678efca873d7a7c87b0d6ef4945fadd', 'details': {'parent_model': '', 'format': 'gguf', 'family': 'llama', 'families': ['llama'], 'parameter_size': '8B', 'quantization_level': 'Q4_0'}}]}
        print(list_models)
        client = Client(host="http://127.0.0.1:11434")
        response = client.generate(model="dolphin-llama3", system="I will give you an object, animal, person or landscape, just create details about it : colors, size, clothes, eyes and other physical details or features in 1 sentence.", prompt=user_prompt, keep_alive=str(keep_alive) + "m")
        print("Ollama response : ", response['response'])
        return (response['response'],)
