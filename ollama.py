import ollama
from ollama import Client  # pip install ollama
import logging
import hashlib
import os

class ollamaLoader:
    @classmethod
    def read_host_from_file(cls, filename='ollama_ip.txt'):
        try:
            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(script_dir, filename)

            # Print the constructed file path for verification
            print(f"Looking for file at: {file_path}")

            with open(file_path, 'r') as f:
                host = f.read().strip()
                if host:
                    logging.info(f"Using host from {file_path}: {host}")
                    return host
                else:
                    logging.warning(f"{file_path} is empty. Falling back to default hosts.")
        except Exception as e:
            logging.error(f"Failed to read host from {file_path}: {e}")
        return None  # Return None if reading fails

    @classmethod
    def get_available_models(cls):
        host = cls.read_host_from_file()
        if host:
            try:
                client = Client(host=host)
                list_models = client.list()
                return [model['name'] for model in list_models['models']]
            except Exception as e:
                logging.error(f"Error fetching models from {host}: {e}")

        # Fallback to default hosts if reading from file fails
        for default_host in ["http://127.0.0.1:11434", "http://0.0.0.0:11434"]:
            try:
                client = Client(host=default_host)
                list_models = client.list()
                return [model['name'] for model in list_models['models']]
            except Exception as e:
                logging.error(f"Error fetching models from {default_host}: {e}")
        return ["none"]  # Return a default model if fetching fails

    @classmethod
    def INPUT_TYPES(cls):
        default_system_prompt = (
            "Describe a specific example of an object, animal, person, or landscape based on a given general idea. "
            "Start with a clear and concise overall description in the first sentence. Then, provide a detailed depiction "
            "of its physical features, focusing on colors, size, clothing, eyes, and other distinguishing characteristics. "
            "Use commas to separate each detail and avoid listing them. Ensure each description is vivid, precise, and "
            "specific to one unique instance of the subject. Refrain from using poetic language and giving it a name.\n"
            "Example input: man\n Example output: \nAn overweight old man sitting on a bench, wearing a blue hat, "
            "yellow pants, orange jacket and black shirt, sunglasses, very long beard, very pale skin, long white hair, "
            "very large nose."
        )
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

        keep_alive_minutes = 1 if keep_1min_in_vram else 0

        host = self.read_host_from_file()
        if host:
            try:
                client = Client(host=host)
                response = client.generate(
                    model=selected_model,
                    system=system_prompt,
                    prompt=user_prompt,
                    keep_alive=f"{keep_alive_minutes}m"
                )
                logging.info(f"Ollama response ({host}): {response['response']}")
                return (response['response'],)
            except Exception as e:
                logging.error(f"Connection to {host} failed: {e}")

        # Fallback to default hosts if reading from file fails
        for default_host in ["http://127.0.0.1:11434", "http://0.0.0.0:11434"]:
            try:
                client = Client(host=default_host)
                response = client.generate(
                    model=selected_model,
                    system=system_prompt,
                    prompt=user_prompt,
                    keep_alive=f"{keep_alive_minutes}m"
                )
                logging.info(f"Ollama response ({default_host}): {response['response']}")
                return (response['response'],)
            except Exception as e:
                logging.error(f"Connection to {default_host} failed: {e}")

        logging.error("All connection attempts failed.")
        return ("Connection to Ollama failed.",)
