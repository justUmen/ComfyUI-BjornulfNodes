import comfy

class LoopSchedulers:
    @classmethod
    def INPUT_TYPES(cls):
        schedulers = ["ALL SCHEDULERS"] + list(comfy.samplers.KSampler.SCHEDULERS)
        return {
            "required": {
                "scheduler": (schedulers,),
            }
        }

    RETURN_TYPES = (comfy.samplers.KSampler.SCHEDULERS,)
    RETURN_NAMES = ("scheduler",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "create_loop_scheduler"
    CATEGORY = "Bjornulf"

    def create_loop_scheduler(self, scheduler):
        if scheduler == "ALL SCHEDULERS":
            return (list(comfy.samplers.KSampler.SCHEDULERS),)
        else:
            return ([scheduler],)