import torch
from pathlib import Path
import os
import numpy as np
import tempfile
import wave

try:
    import faster_whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    print("faster-whisper not found. To use local transcription, install with: pip install faster-whisper")

class SpeechToText:
    def __init__(self):
        self.local_model = None
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_size": (["tiny", "base", "small", "medium", "large-v2"], {"default": "base"}),
            },
            "optional": {
                "AUDIO": ("AUDIO",),
                "audio_path": ("STRING", {"default": None, "forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING",)
    RETURN_NAMES = ("transcript", "detected_language","language_name",)
    FUNCTION = "transcribe_audio"
    CATEGORY = "Bjornulf"

    def tensor_to_wav(self, audio_tensor, sample_rate):
        """Convert audio tensor to temporary WAV file"""
        # Convert tensor to numpy array
        audio_data = audio_tensor.squeeze().numpy()
        
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
        
        # Write WAV file
        with wave.open(temp_file.name, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono audio
            wav_file.setsampwidth(2)  # 2 bytes per sample
            wav_file.setframerate(sample_rate)
            
            # Convert float32 to int16
            audio_data = (audio_data * 32767).astype(np.int16)
            wav_file.writeframes(audio_data.tobytes())
        
        return temp_file.name

    def load_local_model(self, model_size):
        """Load the local Whisper model if not already loaded"""
        if not WHISPER_AVAILABLE:
            return False, "faster-whisper not installed. Install with: pip install faster-whisper"
        
        try:
            if self.local_model is None:
                print(f"Loading local Whisper model ({model_size})...")
                self.local_model = faster_whisper.WhisperModel(model_size, device="cpu", compute_type="int8")
                print("Local model loaded successfully!")
            return True, None
        except Exception as e:
            return False, f"Error loading model: {str(e)}"

    def transcribe_local(self, audio_path, model_size):
        """Transcribe audio using local Whisper model"""
        success, message = self.load_local_model(model_size)
        if not success:
            return False, message, None

        try:
            print("Starting local transcription...")
            segments, info = self.local_model.transcribe(str(audio_path), beam_size=5)
            text = " ".join([segment.text for segment in segments]).strip()
            detected_language = info.language
            print("Local transcription completed successfully!")
            return True, text, detected_language
        except Exception as e:
            return False, f"Error during local transcription: {str(e)}", None

    def transcribe_audio(self, model_size, AUDIO=None, audio_path=None):
        transcript = "No valid audio input provided"
        detected_language = ""
        temp_wav_path = None
        
        try:
            # Determine which audio source to use
            if AUDIO is not None:
                # Convert tensor audio data to WAV file
                waveform = AUDIO['waveform']
                sample_rate = AUDIO['sample_rate']
                temp_wav_path = self.tensor_to_wav(waveform, sample_rate)
                audio_to_process = temp_wav_path
            elif audio_path is not None and os.path.exists(audio_path):
                audio_to_process = audio_path
            else:
                return ("No valid audio input provided", "")

            if audio_to_process:
                success, result, lang = self.transcribe_local(audio_to_process, model_size)
                transcript = result if success else f"Local transcription failed: {result}"
                detected_language = lang if success else ""

        finally:
            # Clean up temporary file if it was created
            if temp_wav_path and os.path.exists(temp_wav_path):
                os.unlink(temp_wav_path)

        #Create detected_language_name based on detected_language, en = English, es = Spanish, fr = French, de = German, etc...
        language_map = {
            "ar": "Arabic", "cs": "Czech", "de": "German", "en": "English",
            "es": "Spanish", "fr": "French", "hi": "Hindi", "hu": "Hungarian",
            "it": "Italian", "ja": "Japanese", "ko": "Korean", "nl": "Dutch",
            "pl": "Polish", "pt": "Portuguese", "ru": "Russian", "tr": "Turkish",
            "zh-cn": "Chinese"
        }
        detected_language_name = language_map.get(detected_language, "Unknown")
        
        return (transcript, detected_language,detected_language_name)