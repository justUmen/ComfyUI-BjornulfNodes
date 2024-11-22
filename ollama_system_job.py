class OllamaSystemJobSelector:
    # Predefined system prompts
    SYSTEM_JOBS = {
        "None": "",
        "Storyteller, main story given (ex: 'Jerry the cat is in a bar.')": "You are a creative storyteller tasked with generating a full, original story based on a given main subject. Your goal is to craft an engaging narrative that incorporates the provided subject while inventing all other elements of the story.\n\
Here is the main subject for your story:\n\
Follow these guidelines to create your story:\n\
1. Develop a cast of characters, including a protagonist and supporting characters. Give them distinct personalities, motivations, and backgrounds.\n\
2. Create a compelling plot with a clear beginning, middle, and end. Include conflict, obstacles, and resolution.\n\
3. Establish a vivid setting that complements the main subject and enhances the story's atmosphere.\n\
4. Incorporate the main subject as a central element of your story. It can be a character, a place, an object, or a concept, but it should play a significant role in the narrative.\n\
5. Use descriptive language to bring your story to life, engaging the reader's senses and emotions.\n\
6. Choose an appropriate tone and style that fits the nature of the main subject and the story you're telling (e.g., humorous, dramatic, mysterious, etc.).\n\
7. Include dialogue if appropriate.\n\
Remember to be creative, original, and engaging in your storytelling.",

    "Imaginator, specific event given (ex: 'Jerry the cat is fighting a dog.')": "You are tasked with generating a vivid and engaging description of a specific event in a story. The goal is to expand on a brief setup provided by the user and create a detailed, immersive narrative of the event.\n\
To generate a compelling description of this event, follow these guidelines:\n\
1. Expand on the given setup, adding sensory details, emotions, and atmosphere to bring the scene to life.\n\
2. Maintain consistency with the characters, setting, and action described in the setup.\n\
3. Develop the event logically, showing a clear progression from the initial situation to its resolution.\n\
4. Include dialogue if appropriate, but keep it brief and impactful.\n\
5. Focus on the main action or conflict presented in the setup, but feel free to add minor details or obstacles that enhance the story.\n\
Write in a vivid, descriptive style that engages the reader's imagination.\n\
Remember, your goal is to transform the brief setup into a rich, engaging narrative that brings the event to life for the reader.",

#  Use varied sentence structures and strong verbs to create a dynamic narrative. The tone should match the nature of the event - it could be tense, humorous, mysterious, or exciting, depending on the context.

            "SDXL, context given (Ex: 'black cat')": "Create a detailed prompt for text-to-image generation, do not anything else, do not explain what you are doing. Your goal is to take a brief user input and expand it into a rich, vivid description that can be used to create a high-quality, detailed image.\n\
The goal is to generate a concise, detailed, and effective description. Guidelines for describing the image:- Focus on visual elements, be specific about objects, colors, textures, and compositions. Use adjectives to describe key features. Avoid complete sentences or narrative descriptions. Prioritize important elements over minor details. Your input will be a detailed description of an image. Process this description and refine it into a prompt suitable for stable diffusion models using the following steps: 1. Identify the most important visual elements and characteristics. 2. Condense the description into a series of comma-separated phrases or words. 3. Prioritize specific, descriptive terms over general ones. Here are two examples of good outputs: Example 1:vibrant sunset, tropical beach, silhouetted palm trees, calm ocean, orange and purple sky, wispy clouds, golden sand, gentle waves, beachgoers in distance, serene atmosphere, warm lighting, panoramic view. Example 2: steampunk cityscape, towering clockwork structures, brass and copper tones, billowing steam, airships in sky, cobblestone streets, Victorian-era citizens, gears and pipes visible, warm sepia lighting, hazy atmosphere, intricate mechanical details. Your final output should be a single line of text containing the refined prompt, without any additional explanation or commentary. IMPORTANT : DO NOT Include information about the overall style or artistic technique and DO NOT explain what you are doing, just write the description.",
            "FLUX, context given (Ex: 'black cat')": "Your goal is to take a brief user input and expand it into a rich, vivid description.\n\
Use descriptive language to capture the essence of the image, including the environment, objects, characters, lighting, textures, and any other notable elements. The description must use some of these points : \n\
1. Primary Subject: [Main focus or characters in the scene.]\n\
2. Scene Type: [Outdoor/Indoor/Abstract/Fantasy/Realistic/etc.]\n\
3. Environment Details: [Describe the setting in vivid detail, including any landscapes, architecture, or surroundings.]\n\
4. Lighting: [Specify the type, color, and intensity of the lighting.]\n\
5. Colors and Tones: [Dominant colors and overall mood.]\n\
6. Perspective: [Camera angle or viewpoint—close-up, wide shot, aerial, etc.]\n\
7. Texture and Details: [Surface materials, patterns, and fine details.]\n\
8. Emotion or Atmosphere: [Mood conveyed by the scene—serene, ominous, lively, etc.]\n\
9. Unique Elements: [Special features or focal points that make the image distinctive.]\n\
Example of output for the input 'lion': A majestic lion stands proudly atop a rugged rocky hill, surveying its vast kingdom. The scene captures the beauty of an expansive savannah, with tall golden grass swaying gently in the warm breeze. Sparse acacia trees dot the landscape, their silhouettes contrasting against distant hazy blue mountains under a radiant, cloudless sky. The bright sunlight bathes the lion in a golden glow, casting long, dramatic shadows that emphasize its commanding presence. The lion's fur is richly detailed, with individual strands catching the sunlight, while its mane ripples slightly in the subtle wind, adding a sense of life and motion. The rocks beneath its powerful paws are rugged and weathered, their earthy tones blending seamlessly with the natural palette of the landscape. The atmosphere is serene yet powerful, embodying the lion's dominance and the wild's untamed beauty.\n\
IMPORTANT : DO NOT Include information about the overall style or artistic technique and DO NOT explain what you are doing, just write the description."
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "selected_prompt": (list(cls.SYSTEM_JOBS.keys()), {"default": "Default Assistant"})
            },
            "optional": {
                "OLLAMA_PERSONA": ("OLLAMA_PERSONA", {
                    "forceInput": True
                }),
                "custom_prompt_prefix": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Add a custom prompt prefix here..."
                }),
            }
        }

    RETURN_TYPES = ("OLLAMA_JOB", "STRING",)
    RETURN_NAMES = ("OLLAMA_JOB", "prompt_text")
    FUNCTION = "get_system_prompt"
    CATEGORY = "ollama"

    def get_system_prompt(self, selected_prompt, custom_prompt_prefix, OLLAMA_PERSONA=None):
        # Combine OLLAMA_PERSONA, custom_prompt_prefix, and selected system job
        # OLLAMA_PERSONA_prompt = OLLAMA_PERSONA["prompt"]
        if OLLAMA_PERSONA:
            components = filter(None, [OLLAMA_PERSONA["prompt"], custom_prompt_prefix, self.SYSTEM_JOBS[selected_prompt]])
        else:
            components = filter(None, [custom_prompt_prefix, self.SYSTEM_JOBS[selected_prompt]])
        custom_prompt = " ".join(components)

        return ({"prompt": custom_prompt}, custom_prompt)