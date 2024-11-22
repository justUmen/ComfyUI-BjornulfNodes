import os
import random
from folder_paths import get_filename_list, get_full_path
import comfy.sd
import comfy.utils

class RandomLoraSelector:
    @classmethod
    def INPUT_TYPES(cls):
        lora_list = get_filename_list("loras")
        optional_inputs = {}
        
        # Add a default value if lora_list is empty
        if not lora_list:
            lora_list = ["none"]
            
        for i in range(1, 11):
            optional_inputs[f"lora_{i}"] = (lora_list, {"default": lora_list[0]})
        
        optional_inputs["seed"] = ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})

        return {
            "required": {
                "number_of_loras": ("INT", {"default": 3, "min": 1, "max": 20, "step": 1}),
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "strength_model": ("FLOAT", {"default": 1.0, "min": -100.0, "max": 100.0, "step": 0.01}),
                "strength_clip": ("FLOAT", {"default": 1.0, "min": -100.0, "max": 100.0, "step": 0.01}),
            },
            "optional": optional_inputs
        }

    RETURN_TYPES = ("MODEL", "CLIP", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("model", "clip", "lora_path", "lora_name", "lora_folder")
    FUNCTION = "random_select_lora"
    CATEGORY = "Bjornulf"

    def random_select_lora(self, number_of_loras, model, clip, strength_model, strength_clip, seed, **kwargs):
        random.seed(seed)

        # Collect available Loras from kwargs, excluding "none"
        available_loras = [
            kwargs[f"lora_{i}"] for i in range(1, number_of_loras + 1) 
            if f"lora_{i}" in kwargs and kwargs[f"lora_{i}"] and kwargs[f"lora_{i}"] != "none"
        ]
        
        # Return original model and clip if no valid LoRAs are available
        if not available_loras:
            return (model, clip, "", "", "")
        
        # Randomly select a Lora
        selected_lora = random.choice(available_loras)
        
        # Get the Lora name (without folders or extensions)
        lora_name = os.path.splitext(os.path.basename(selected_lora))[0]
        
        # Get the full path to the selected Lora
        lora_path = get_full_path("loras", selected_lora)
        
        # Get the folder name where the Lora is located
        lora_folder = os.path.basename(os.path.dirname(lora_path))
        
        # Load the Lora file
        lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
        
        # Apply the Lora
        model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora, strength_model, strength_clip)
        
        return (model_lora, clip_lora, lora_path, lora_name, lora_folder)