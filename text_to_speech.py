import requests
import numpy as np
import io
import torch
from pydub import AudioSegment
from pydub.playback import play
import urllib.parse
import os
import sys
import random
import re
from typing import Dict, Any, List, Tuple

class Everything(str):
    def __ne__(self, __value: object) -> bool:
        return False

language_map = {
    "ar": "Arabic", "cs": "Czech", "de": "German", "en": "English",
    "es": "Spanish", "fr": "French", "hi": "Hindi", "hu": "Hungarian",
    "it": "Italian", "ja": "Japanese", "ko": "Korean", "nl": "Dutch",
    "pl": "Polish", "pt": "Portuguese", "ru": "Russian", "tr": "Turkish",
    "zh-cn": "Chinese"
}

class TextToSpeech:
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        speakers_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "speakers")
        speaker_options = [os.path.relpath(os.path.join(root, file), speakers_dir)
                           for root, _, files in os.walk(speakers_dir)
                           for file in files if file.endswith(".wav")]
        
        speaker_options = speaker_options or ["No WAV files found"]
        
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "language": (list(language_map.values()), {
                    "default": language_map["en"],
                    "display": "dropdown"
                }),
                "speaker_wav": (speaker_options, {
                    "default": speaker_options[0],
                    "display": "dropdown"
                }),
                "autoplay": ("BOOLEAN", {"default": True}),
                "save_audio": ("BOOLEAN", {"default": True}),
                "overwrite": ("BOOLEAN", {"default": False}),
                "seed": ("INT", {"default": 0}),
            },
            "optional": {
                "connect_to_workflow": (Everything("*"), {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("AUDIO", "STRING", "STRING", "FLOAT")
    RETURN_NAMES = ("AUDIO", "audio_path", "audio_full_path", "audio_duration")
    FUNCTION = "generate_audio"
    CATEGORY = "Bjornulf"
    
    @staticmethod
    def get_language_code(language_name: str) -> str:
        return next((code for code, name in language_map.items() if name == language_name), "en")
    
    @staticmethod
    def sanitize_text(text: str) -> str:
        return re.sub(r'[^\w\s-]', '', text).replace(' ', '_')[:50]
    
    def generate_audio(self, text: str, language: str, autoplay: bool, seed: int,
                       save_audio: bool, overwrite: bool, speaker_wav: str,
                       connect_to_workflow: Any = None) -> Tuple[Dict[str, Any], str, str, float]:
        language_code = self.get_language_code(language)
        sanitized_text = self.sanitize_text(text)

        save_path = os.path.join("Bjornulf_TTS", language, speaker_wav, f"{sanitized_text}.wav")
        full_path = os.path.abspath(save_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        if os.path.exists(full_path) and not overwrite:
            print(f"Using existing audio file: {full_path}")
            audio_data = self.load_audio_file(full_path)
        else:
            audio_data = self.create_new_audio(text, language_code, speaker_wav, seed)
            if save_audio:
                self.save_audio_file(audio_data, full_path)

        audio_output, _, duration = self.process_audio_data(autoplay, audio_data, full_path if save_audio else None)
        return (audio_output, save_path, full_path, duration)

    def create_new_audio(self, text: str, language_code: str, speaker_wav: str, seed: int) -> io.BytesIO:
        random.seed(seed)
        if speaker_wav == "No WAV files found":
            print("Error: No WAV files available for text-to-speech.")
            return io.BytesIO()

        encoded_text = urllib.parse.quote(text)
        url = f"http://localhost:8020/tts_stream?language={language_code}&speaker_wav={speaker_wav}&text={encoded_text}"
        
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            audio_data = io.BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                audio_data.write(chunk)
            
            audio_data.seek(0)
            return audio_data

        except requests.RequestException as e:
            print(f"Error generating audio: {e}")
            return io.BytesIO()
        except Exception as e:
            print(f"Unexpected error: {e}")
            return io.BytesIO()

    def play_audio(self, audio: AudioSegment) -> None:
        if sys.platform.startswith('win'):
            try:
                import winsound
                winsound.PlaySound(audio.raw_data, winsound.SND_MEMORY)
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            play(audio)
            
    def process_audio_data(self, autoplay: bool, audio_data: io.BytesIO, save_path: str) -> Tuple[Dict[str, Any], str, float]:
        try:
            audio = AudioSegment.from_mp3(audio_data)
            sample_rate = audio.frame_rate
            num_channels = audio.channels
            audio_np = np.array(audio.get_array_of_samples()).astype(np.float32)
            audio_np /= np.iinfo(np.int16).max
            
            audio_np = audio_np.reshape(-1, num_channels).T if num_channels > 1 else audio_np.reshape(1, -1)
            
            audio_tensor = torch.from_numpy(audio_np)
            
            if autoplay:
                self.play_audio(audio)
            
            duration = len(audio) / 1000.0  # Convert milliseconds to seconds
            
            return ({"waveform": audio_tensor.unsqueeze(0), "sample_rate": sample_rate}, save_path or "", duration)
    
        except Exception as e:
            print(f"Error processing audio data: {e}")
            return ({"waveform": torch.zeros(1, 1, 1, dtype=torch.float32), "sample_rate": 22050}, "", 0.0)

    def save_audio_file(self, audio_data: io.BytesIO, save_path: str) -> None:
        try:
            with open(save_path, 'wb') as f:
                f.write(audio_data.getvalue())
            print(f"Audio saved to: {save_path}")
        except Exception as e:
            print(f"Error saving audio file: {e}")

    def load_audio_file(self, file_path: str) -> io.BytesIO:
        try:
            with open(file_path, 'rb') as f:
                audio_data = io.BytesIO(f.read())
            return audio_data
        except Exception as e:
            print(f"Error loading audio file: {e}")
            return io.BytesIO()