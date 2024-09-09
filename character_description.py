import os
import json

class CharacterDescriptionGenerator:
    @classmethod
    def INPUT_TYPES(s):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        characters_folder = os.path.join(current_dir, "characters")
        
        if not os.path.exists(characters_folder):
            print(f"Warning: 'characters' folder not found at {characters_folder}")
            return {"required": {"character_file": (["No character files found"],)}}
        
        json_files = [f for f in os.listdir(characters_folder) if f.endswith('.json')]
        
        if not json_files:
            print(f"Warning: No JSON files found in {characters_folder}")
            return {"required": {"character_file": (["No character files found"],)}}
        
        return {"required": {"character_file": (json_files,)}}
    
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("sentences", "words", "name")
    FUNCTION = "generate_descriptions"
    CATEGORY = "Bjornulf"

    def generate_descriptions(self, character_file):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "characters", character_file)

        if not os.path.exists(file_path):
            return (f"Error: File {character_file} not found.", "")

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

            name = data.get('name', 'Unknown')
            nationality = data.get('nationality', 'Unknown')
            age = data.get('age', 'Unknown')
            gender = data.get('gender', 'Unknown').lower()
            height = data.get('height', 'Unknown')
            weight = data.get('weight', 'Unknown')
            body_type = data.get('body_type', {})
            face = data.get('face', {})
            eyes = face.get('eyes', {})
            hair = data.get('hair', {})

            pronouns = {
                'subject': 'They',
                'object': 'them',
                'possessive': 'their'
            }
            if gender in ['female', 'f']:
                pronouns = {'subject': 'She', 'object': 'her', 'possessive': 'her'}
            elif gender in ['male', 'm']:
                pronouns = {'subject': 'He', 'object': 'him', 'possessive': 'his'}

            body_desc = f"{body_type.get('build', '')} and {body_type.get('figure', '')}"
            eyes_desc = f"{eyes.get('color', '')} {eyes.get('shape', '')} eyes that appear {eyes.get('feature', '')}"
            hair_desc = f"{hair.get('length', '')} {hair.get('color', '')} {hair.get('texture', '')} hair"

            sentences = (
                f"{name} is a {age}-year-old {nationality} {gender.lower()}. "
                f"{pronouns['subject']} stands at {height} and weighs {weight}. "
                f"{pronouns['subject']} has a {body_desc} build, with {body_type.get('shoulders', '')} shoulders, "
                f"a {body_type.get('waist', '')} waist, and {body_type.get('hips', '')} hips. "
                f"{pronouns['possessive'].capitalize()} face is characterized by {eyes_desc}, complemented by {hair_desc} "
                f"that {pronouns['subject'].lower()} usually styles {hair.get('style', '')}. "
                f"{name}'s complexion is {face.get('complexion', '')}, with a {face.get('shape', '')} face shape, "
                f"a {face.get('nose', '')} nose, {face.get('lips', '')} lips, {face.get('cheekbones', '')} cheekbones, "
                f"and a {face.get('jawline', '')} jawline."
            )
            
            words_list = [
                f"{age} years old",
                f"{nationality}",
                f"{gender}",
                f"{height} tall",
                f"{weight}",
                f"{body_type.get('build', '')} build",
                f"{body_type.get('figure', '')} figure",
                f"{body_type.get('shoulders', '')} shoulders",
                f"{body_type.get('waist', '')} waist",
                f"{body_type.get('hips', '')} hips",
                f"{eyes.get('color', '')} eyes",
                f"{eyes.get('shape', '')} eyes",
                f"{eyes.get('feature', '')} eyes",
                f"{hair.get('length', '')} hair",
                f"{hair.get('color', '')} hair",
                f"{hair.get('texture', '')} hair",
                f"{hair.get('style', '')}",
                f"{face.get('complexion', '')} complexion",
                f"{face.get('shape', '')} face",
                f"{face.get('nose', '')} nose",
                f"{face.get('lips', '')} lips",
                f"{face.get('cheekbones', '')} cheekbones",
                f"{face.get('jawline', '')} jawline"
            ]
            words = ", ".join(words_list)

            return (sentences, words, character_file.replace('.json', ''))

        except Exception as e:
            return (f"Error processing {character_file}: {str(e)}", "")
