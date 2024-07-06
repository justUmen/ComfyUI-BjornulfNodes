import comfy

class LoopSamplers:
    @classmethod
    def INPUT_TYPES(cls):
        samplers = ["ALL SAMPLERS"] + list(comfy.samplers.KSampler.SAMPLERS)
        return {
            "required": {
                "sampler_name": (samplers,),
            }
        }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,)
    RETURN_NAMES = ("sampler_name",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "create_loop_sampler"
    CATEGORY = "Bjornulf"

    def create_loop_sampler(self, sampler_name):
        if sampler_name == "ALL SAMPLERS":
            return (list(comfy.samplers.KSampler.SAMPLERS),)
        else:
            return ([sampler_name],)