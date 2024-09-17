import os
import random
from folder_paths import get_filename_list, get_full_path
import comfy.sd

class RandomModelSelector:
    @classmethod
    def INPUT_TYPES(cls):
        model_list = get_filename_list("checkpoints")
        optional_inputs = {}
        
        for i in range(1, 11):
            optional_inputs[f"model_{i}"] = (model_list, {"default": model_list[min(i-1, len(model_list)-1)]})
        
        optional_inputs["seed"] = ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})

        return {
            "required": {
                "number_of_models": ("INT", {"default": 3, "min": 1, "max": 20, "step": 1}),
            },
            "optional": optional_inputs
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("model", "clip", "vae", "model_path", "model_name", "model_folder")
    FUNCTION = "random_select_model"
    CATEGORY = "Bjornulf"

    def random_select_model(self, number_of_models, seed, **kwargs):
        random.seed(seed)
        
        available_models = [kwargs[f"model_{i}"] for i in range(1, number_of_models + 1) if f"model_{i}" in kwargs]
        
        if not available_models:
            raise ValueError("No models selected")
        
        selected_model = random.choice(available_models)
        
        # Extract just the name of the model (no folders and no extensions)
        model_name = os.path.splitext(os.path.basename(selected_model))[0]
        
        # Get the full path of the selected model
        model_path = get_full_path("checkpoints", selected_model)
        
        # Get the folder of the selected model (Hopefully people use that to organize their models...)
        model_folder = os.path.basename(os.path.dirname(model_path))
        
        # Load the model
        loaded_objects = comfy.sd.load_checkpoint_guess_config(model_path)
        
        # Unpack only the values we need
        model = loaded_objects[0]
        clip = loaded_objects[1]
        vae = loaded_objects[2]
        
        return (model, clip, vae, model_path, model_name, model_folder)
