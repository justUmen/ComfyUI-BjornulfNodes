import ollama
from ollama import Client  # pip install ollama
import logging
import hashlib

class ollamaLoader:
    @classmethod
    def get_available_models(cls):
        try:
            # First try with 127.0.0.1
            client = Client(host="http://127.0.0.1:11434")
            list_models = client.list()  # Assuming list() is part of the Client class
            return [model['name'] for model in list_models['models']]
        except Exception as e1:
            print(f"Error fetching models from 127.0.0.1: {e1}")
            try:
                # Fallback to 0.0.0.0
                client = Client(host="http://0.0.0.0:11434")
                list_models = client.list()
                return [model['name'] for model in list_models['models']]
            except Exception as e2:
                print(f"Error fetching models from 0.0.0.0: {e2}")
                return ["none"]  # Return a default model if fetching fails

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
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "keep_1min_in_vram": ("BOOLEAN", {"default": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ollama_response",)
    FUNCTION = "connect_2_ollama"
    CATEGORY = "Bjornulf"

    def __init__(self):
        self.last_content_hash = None

    def connect_2_ollama(self, user_prompt, selected_model, system_prompt, keep_1min_in_vram, seed):
        # Generate a hash of the current content
        content_hash = hashlib.md5((user_prompt + selected_model + system_prompt).encode()).hexdigest()

        # Check if the content has changed
        if content_hash != self.last_content_hash:
            # Content has changed, use the provided seed
            self.last_content_hash = content_hash
        else:
            # Content hasn't changed, set seed to None to prevent randomization
            seed = None
        
        keep_alive_minutes = 0
        if(keep_1min_in_vram):
            keep_alive_minutes = 1
            
        keep_alive = 0
        # client = Client(host="http://0.0.0.0:11434")
        # response = client.generate(
        #     model=selected_model,
        #     system=system_prompt,
        #     prompt=user_prompt,
        #     keep_alive=str(keep_alive_minutes) + "m"
        # )
        try:
            # First attempt with 127.0.0.1
            client = Client(host="http://127.0.0.1:11434")
            response = client.generate(
                model=selected_model,
                system=system_prompt,
                prompt=user_prompt,
                keep_alive=str(keep_alive_minutes) + "m"
            )
            logging.info("Ollama response (127.0.0.1): " + response['response'])
        except Exception as e:
            logging.warning(f"Connection to 127.0.0.1 failed: {e}")
            try:
                # Fallback to 0.0.0.0 if 127.0.0.1 fails
                client = Client(host="http://0.0.0.0:11434")
                response = client.generate(
                    model=selected_model,
                    system=system_prompt,
                    prompt=user_prompt,
                    keep_alive=str(keep_alive_minutes) + "m"
                )
                logging.info("Ollama response (0.0.0.0): " + response['response'])
            except Exception as e:
                logging.error(f"Connection to 0.0.0.0 also failed: {e}")
        logging.info("Ollama response : " + response['response'])
        return (response['response'],)