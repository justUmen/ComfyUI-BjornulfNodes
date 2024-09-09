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
            age = data.get('age', 'Unknown')
            gender = data.get('gender', 'Unknown').lower()
            height = data.get('height', 'Unknown')
            weight = data.get('weight', 'Unknown')

            face = data.get('face', {})
            eyes = face.get('eyes', {})
            hair = face.get('hair', {})
            body_type = face.get('body_type', {})

            # Define pronouns based on gender
            if gender in ['female', 'f']:
                pronouns = {
                    'subject': 'She',
                    'object': 'her',
                    'possessive': 'her'
                }
            elif gender in ['male', 'm']:
                pronouns = {
                    'subject': 'He',
                    'object': 'him',
                    'possessive': 'his'
                }
            else:
                pronouns = {
                    'subject': 'They',
                    'object': 'them',
                    'possessive': 'their'
                }

            # Generate sentences description
            sentences = f"{name} is a {age}-year-old {gender} standing {height} tall and weighing {weight}. "

            if face:
                sentences += f"{pronouns['subject']} has an {face.get('shape', 'unknown').lower()} face with a {face.get('complexion', 'unknown').lower()} complexion. "
                
                if eyes:
                    sentences += f"{pronouns['possessive'].capitalize()} {eyes.get('color', 'unknown').lower()} eyes are {eyes.get('shape', 'unknown').lower()} "
                    sentences += f"with {eyes.get('feature', 'unknown').lower()}. "
                
                sentences += f"{pronouns['possessive'].capitalize()} nose is {face.get('nose', 'unknown').lower()}, and {pronouns['possessive']} lips are {face.get('lips', 'unknown').lower()}. "
                sentences += f"{pronouns['subject']} has {face.get('cheekbones', 'unknown').lower()} cheekbones and a {face.get('jawline', 'unknown').lower()} jawline. "

            if hair:
                sentences += f"{name}'s {hair.get('color', 'unknown')} hair is {hair.get('length', 'unknown').lower()} and {hair.get('texture', 'unknown').lower()}, "
                sentences += f"{hair.get('style', 'unknown').lower()}. "

            if body_type:
                sentences += f"{pronouns['subject']} has a {body_type.get('build', 'unknown').lower()} body type with a {body_type.get('figure', 'unknown').lower()} figure, "
                sentences += f"{body_type.get('shoulders', 'unknown').lower()} shoulders, a {body_type.get('waist', 'unknown').lower()} waist, "
                sentences += f"and {body_type.get('hips', 'unknown').lower()} hips."

            
            # Generate words description
            words_list = [
                f"{age} years old",
                gender,
                f"{height} tall",
                f"{weight} weight",
                face.get('shape', 'unknown').lower() + " face",
                face.get('complexion', 'unknown').lower() + " complexion",
                eyes.get('color', 'unknown').lower() + " eyes",
                eyes.get('shape', 'unknown').lower() + " eyes",
                eyes.get('feature', 'unknown').lower() + " eyelashes",
                face.get('nose', 'unknown').lower() + " nose",
                face.get('lips', 'unknown').lower() + " lips",
                face.get('cheekbones', 'unknown').lower() + " cheekbones",
                face.get('jawline', 'unknown').lower() + " jawline",
                hair.get('color', 'unknown') + " hair",
                hair.get('length', 'unknown').lower() + " hair",
                hair.get('texture', 'unknown').lower() + " hair",
                hair.get('style', 'unknown').lower() + " hairstyle",
                body_type.get('build', 'unknown').lower() + " build",
                body_type.get('figure', 'unknown').lower() + " figure",
                body_type.get('shoulders', 'unknown').lower() + " shoulders",
                body_type.get('waist', 'unknown').lower() + " waist",
                body_type.get('hips', 'unknown').lower() + " hips"
            ]
            words = ", ".join(words_list)
            
            return (sentences, words, character_file.replace('.json', ''))
        
        except Exception as e:
            return (f"Error processing {character_file}: {str(e)}", "")