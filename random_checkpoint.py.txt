import random

class RandomCheckpoint:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number_of_inputs": ("INT", {"default": 2, "min": 2, "max": 10, "step": 1}),
                "model_1": ("MODEL", {"forceInput": True}),
                "clip_1": ("CLIP", {"forceInput": True}),
                "vae_1": ("VAE", {"forceInput": True}),
                "model_2": ("MODEL", {"forceInput": True}),
                "clip_2": ("CLIP", {"forceInput": True}),
                "vae_2": ("VAE", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "random_select"

    def random_select(self, number_of_inputs, **kwargs):
        selected_index = random.randint(1, number_of_inputs)
        
        selected_model = kwargs[f"model_{selected_index}"]
        selected_clip = kwargs[f"clip_{selected_index}"]
        selected_vae = kwargs[f"vae_{selected_index}"]
        
        return (selected_model, selected_clip, selected_vae)
