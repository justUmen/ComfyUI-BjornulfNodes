class LoopModelClipVae:
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
            },
            "hidden": {
                **{f"model_{i}": ("MODEL", {"forceInput": True}) for i in range(3, 11)},
                **{f"clip_{i}": ("CLIP", {"forceInput": True}) for i in range(3, 11)},
                **{f"vae_{i}": ("VAE", {"forceInput": True}) for i in range(3, 11)}
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "return_all"
    OUTPUT_IS_LIST = (True, True, True)
    CATEGORY = "Bjornulf"

    def return_all(self, number_of_inputs, **kwargs):
        models = [kwargs[f"model_{i}"] for i in range(1, number_of_inputs + 1) if f"model_{i}" in kwargs]
        clips = [kwargs[f"clip_{i}"] for i in range(1, number_of_inputs + 1) if f"clip_{i}" in kwargs]
        vaes = [kwargs[f"vae_{i}"] for i in range(1, number_of_inputs + 1) if f"vae_{i}" in kwargs]
        
        return (models, clips, vaes)