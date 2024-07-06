import comfy

class LoopCombosSamplersSchedulers:
    combinations = [
        "sgm_uniform/euler", "sgm_uniform/dpm_2", "sgm_uniform/dpmpp_2m", "sgm_uniform/lcm",
        "sgm_uniform/ddim", "sgm_uniform/uni_pc",

        "normal/ddim", "normal/uni_pc", "normal/euler", "normal/heunpp2", "normal/dpm_2",

        "ddim_uniform/euler", "ddim_uniform/dpm_2", "ddim_uniform/lcm", "ddim_uniform/uni_pc",

        "simple/euler", "simple/heun", "simple/heunpp2", "simple/dpmpp_2m", "simple/lcm", "simple/ipndm", "simple/uni_pc",

        "exponential/dpm_adaptive"
    ]
    # "normal/uni_pc_bh2", "ddim_uniform/uni_pc_bh2", "simple/uni_pc_bh2", "sgm_uniform/uni_pc_bh2"
    @classmethod
    def INPUT_TYPES(cls):
        # Generate the list of combinations from specified pairs
        combi_list = ["ALL 6 COMBINATIONS (sgm_uniform)", "ALL 5 COMBINATIONS (normal)", "ALL 5 COMBINATIONS (ddim_uniform)", "ALL 7 COMBINATIONS (simple)"] + cls.combinations
        return {
            "required": {
                "combination": (combi_list,),
            }
        }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS, comfy.samplers.KSampler.SCHEDULERS,)
    RETURN_NAMES = ("sampler_name", "scheduler",)
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "create_loop_combination"
    CATEGORY = "Bjornulf"

    def create_loop_combination(self, combination):
        if combination == "ALL 6 COMBINATIONS (sgm_uniform)":
            return (["euler", "dpm_2", "dpmpp_2m", "lcm", "ddim", "uni_pc"], "sgm_uniform",) #, "uni_pc_bh2" uni_pc_bh2 is too similar to exist....
        elif combination == "ALL 5 COMBINATIONS (normal)":
            return (["ddim", "uni_pc", "euler", "heunpp2", "dpm_2"], "normal",) #, "uni_pc_bh2"
        elif combination == "ALL 5 COMBINATIONS (ddim_uniform)":
            return (["euler", "dpm_2", "lcm", "ddim", "uni_pc"], "ddim_uniform",) #, "uni_pc_bh2"
        elif combination == "ALL 7 COMBINATIONS (simple)":
            return (["euler", "heun", "heunpp2", "dpmpp_2m", "lcm", "ipndm", "uni_pc"], "simple",) #, "uni_pc_bh2"
        else:
            # Split the input and output the selected sampler and scheduler
            scheduler, sampler = combination.split("/")
            # return [(sampler, scheduler,)]
            return ([sampler], scheduler,)

# + ("exponential", "dpm_adaptive")

# TESTED GOOD WITH SD3, modelsampling 5 / CFG 3 / 28 steps

# sgm_uniform + euler
# sgm_uniform + dpm_2
# sgm_uniform + dpmpp_2m
# sgm_uniform + lcm
# sgm_uniform + ddim
# sgm_uniform + uni_pc
# sgm_uniform + uni_pc_bh2

# normal + ddim
# normal + uni_pc
# normal + uni_pc_bh2
# normal + euler
# normal + heunpp2
# normal + dpm_2

# ddim_uniform + euler
# ddim_uniform + dpm_2
# ddim_uniform + lcm
# ddim_uniform + uni_pc
# ddim_uniform + uni_pc_bh2

# simple + euler
# simple + heun
# simple + heunpp2
# simple + dpmpp_2m
# simple + lcm
# simple + ipndm
# simple + uni_pc
# simple + uni_pc_bh2

# exponential + dpm_adaptive