import requests
import numpy as np
import io
import torch
from pydub import AudioSegment
import urllib.parse
import os

class TextToSpeech:
    @classmethod
    def INPUT_TYPES(cls):
        # speakers_dir = "speakers"
        speakers_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "speakers")
        speaker_options = []

        for root, dirs, files in os.walk(speakers_dir):
            for file in files:
                if file.endswith(".wav"):
                    rel_path = os.path.relpath(os.path.join(root, file), speakers_dir)
                    speaker_options.append(rel_path)

        # If no .wav files are found, add a default option
        if not speaker_options:
            speaker_options.append("No WAV files found")

        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "language": (["ar", "cs", "de", "en", "es", "fr", "hi", "hu", "it", "ja", "ko", "nl", "pl", "pt", "ru", "tr", "zh-cn"], {
                    "default": "en",
                    "display": "dropdown",
                    "labels": ["Arabic", "Czech", "German", "English", "Spanish", "French", "Hindi", "Hungarian", "Italian", "Japanese", "Korean", "Dutch", "Polish", "Portuguese", "Russian", "Turkish", "Chinese"]
                }),
                "speaker_wav": (speaker_options, {
                    "default": speaker_options[0],
                    "display": "dropdown"
                }),
            }
        }

    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "generate_audio"
    CATEGORY = "audio"

    def generate_audio(self, text, language, speaker_wav):
        # Check if a valid speaker_wav was selected
        if speaker_wav == "No WAV files found":
            print("Error: No WAV files available for text-to-speech.")
            return ({"waveform": torch.zeros(1, 1, 1, dtype=torch.float32), "sample_rate": 22050},)
        encoded_text = urllib.parse.quote(text)  # Encode spaces and special characters
        url = f"http://localhost:8020/tts_stream?language={language}&speaker_wav={speaker_wav}&text={encoded_text}"
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            audio_data = io.BytesIO()
            for chunk in response.iter_content(chunk_size=8192):
                audio_data.write(chunk)
            
            audio_data.seek(0)
            return self.process_audio_data(audio_data)

        except requests.RequestException as e:
            print(f"Error generating audio: {e}")
            return ({"waveform": torch.zeros(1, 1, 1, dtype=torch.float32), "sample_rate": 22050},)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return ({"waveform": torch.zeros(1, 1, 1, dtype=torch.float32), "sample_rate": 22050},)

    def process_audio_data(self, audio_data):
        try:
            # Load MP3 data
            audio = AudioSegment.from_mp3(audio_data)
            
            # Get audio properties
            sample_rate = audio.frame_rate
            num_channels = audio.channels
            
            # Convert to numpy array
            audio_np = np.array(audio.get_array_of_samples()).astype(np.float32)
            
            # Normalize to [-1, 1]
            audio_np /= np.iinfo(np.int16).max
            
            print(f"Raw audio data shape: {audio_np.shape}")
            
            # Reshape to (num_channels, num_samples)
            if num_channels == 1:
                audio_np = audio_np.reshape(1, -1)
            else:
                audio_np = audio_np.reshape(-1, num_channels).T
            
            # Convert to torch tensor
            audio_tensor = torch.from_numpy(audio_np)
            
            print(f"Final audio tensor shape: {audio_tensor.shape}")
            print(f"Audio data type: {audio_tensor.dtype}")
            print(f"Audio data min: {audio_tensor.min()}, max: {audio_tensor.max()}")
            
            # Wrap the tensor in a list to match the expected format
            return ({"waveform": audio_tensor.unsqueeze(0), "sample_rate": sample_rate},)
    
        except Exception as e:
            print(f"Error processing audio data: {e}")
            raise

