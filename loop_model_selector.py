import os
from folder_paths import get_filename_list, get_full_path
import comfy.sd

class LoopModelSelector:
    @classmethod
    def INPUT_TYPES(cls):
        model_list = get_filename_list("checkpoints")
        optional_inputs = {}
        
        for i in range(1, 11):
            optional_inputs[f"model_{i}"] = (model_list, {"default": model_list[min(i-1, len(model_list)-1)]})

        return {
            "required": {
                "number_of_models": ("INT", {"default": 3, "min": 1, "max": 20, "step": 1}),
            },
            "optional": optional_inputs
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("model", "clip", "vae", "model_path", "model_name", "model_folder")
    FUNCTION = "select_models"
    CATEGORY = "Bjornulf"
    OUTPUT_IS_LIST = (True, True, True, True, True, True)

    def select_models(self, number_of_models, **kwargs):
        # Collect available models from kwargs
        available_models = [
            kwargs[f"model_{i}"] for i in range(1, number_of_models + 1) if f"model_{i}" in kwargs and kwargs[f"model_{i}"]
        ]
        
        # Raise an error if no models are available
        if not available_models:
            raise ValueError("No models selected")
        
        models = []
        clips = []
        vaes = []
        model_paths = []
        model_names = []
        model_folders = []
        
        for selected_model in available_models:
            # Get the model name (without folders or extensions)
            model_name = os.path.splitext(os.path.basename(selected_model))[0]
            
            # Get the full path to the selected model
            model_path = get_full_path("checkpoints", selected_model)
            
            # Get the folder name where the model is located
            model_folder = os.path.basename(os.path.dirname(model_path))
            
            # Load the model using ComfyUI's checkpoint loader
            loaded_objects = comfy.sd.load_checkpoint_guess_config(model_path)
            
            # Unpack only the values we need
            model, clip, vae = loaded_objects[:3]
            
            models.append(model)
            clips.append(clip)
            vaes.append(vae)
            model_paths.append(model_path)
            model_names.append(model_name)
            model_folders.append(model_folder)
        
        return (models, clips, vaes, model_paths, model_names, model_folders)