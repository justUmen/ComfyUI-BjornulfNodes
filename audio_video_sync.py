import torch
import torchaudio
import os
import subprocess
from datetime import datetime
import math

class AudioVideoSync:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "video_path": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("AUDIO", "STRING", "STRING", "FLOAT")
    RETURN_NAMES = ("synced_audio", "audio_path", "synced_video_path", "video_fps")
    FUNCTION = "sync_audio_video"
    CATEGORY = "audio"

    # def get_video_duration(self, video_path):
    #     cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video_path]
    #     result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #     duration = float(result.stdout)
    #     return math.ceil(duration * 10) / 10
    
    def get_video_duration(self, video_path):
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', video_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return float(result.stdout)

    def get_video_fps(self, video_path):
        cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_packets', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', video_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        fps = result.stdout.strip()
        if '/' in fps:
            num, den = map(float, fps.split('/'))
            return num / den
        return float(fps)

    def sync_audio_video(self, audio, video_path):
        if not isinstance(audio, dict) or 'waveform' not in audio or 'sample_rate' not in audio:
            raise ValueError("Expected audio input to be a dictionary with 'waveform' and 'sample_rate' keys")

        audio_data = audio['waveform']
        sample_rate = audio['sample_rate']

        print(f"Audio data shape: {audio_data.shape}")
        print(f"Sample rate: {sample_rate}")

        # Calculate video duration
        video_duration = self.get_video_duration(video_path)

        # Calculate audio duration
        audio_duration = audio_data.shape[-1] / sample_rate

        print(f"Video duration: {video_duration}")
        print(f"Audio duration: {audio_duration}")

        # Calculate the desired audio duration and number of video repetitions
        if audio_duration <= video_duration:
            target_duration = video_duration
            repetitions = 1
        else:
            repetitions = math.ceil(audio_duration / video_duration)
            target_duration = video_duration * repetitions

        # Calculate the number of samples to add
        current_samples = audio_data.shape[-1]
        target_samples = int(target_duration * sample_rate)
        samples_to_add = target_samples - current_samples

        print(f"Current samples: {current_samples}, Target samples: {target_samples}, Samples to add: {samples_to_add}")

        if samples_to_add > 0:
            # Create silence
            if audio_data.dim() == 3:
                silence_shape = (audio_data.shape[0], audio_data.shape[1], samples_to_add)
            else:  # audio_data.dim() == 2
                silence_shape = (audio_data.shape[0], samples_to_add)
            
            silence = torch.zeros(silence_shape, dtype=audio_data.dtype, device=audio_data.device)
            
            # Append silence to the audio
            synced_audio = torch.cat((audio_data, silence), dim=-1)
        else:
            synced_audio = audio_data

        print(f"Synced audio shape: {synced_audio.shape}")

        # Save the synced audio file and get the file path
        audio_path = self.save_audio(synced_audio, sample_rate)

        # Create and save the synced video
        synced_video_path = self.create_synced_video(video_path, repetitions)

        video_fps = self.get_video_fps(video_path)
        
        # Return the synced audio data, audio file path, and synced video path
        return ({"waveform": synced_audio, "sample_rate": sample_rate}, audio_path, synced_video_path, video_fps)   

    def save_audio(self, audio_tensor, sample_rate):
        # Create the sync_audio folder if it doesn't exist
        os.makedirs("Bjornulf/sync_audio", exist_ok=True)

        # Generate a unique filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Bjornulf/sync_audio/synced_audio_{timestamp}.wav"

        # Ensure audio_tensor is 2D
        if audio_tensor.dim() == 3:
            audio_tensor = audio_tensor.squeeze(0)  # Remove batch dimension
        elif audio_tensor.dim() == 1:
            audio_tensor = audio_tensor.unsqueeze(0)  # Add channel dimension

        # Save the audio file
        torchaudio.save(filename, audio_tensor, sample_rate)
        print(f"Synced audio saved to: {filename}")

        # Return the full path to the saved audio file
        return os.path.abspath(filename)

    def create_synced_video(self, video_path, repetitions):
        # Create the sync_video folder if it doesn't exist
        os.makedirs("Bjornulf/sync_video", exist_ok=True)

        # Generate a unique filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"Bjornulf/sync_video/synced_video_{timestamp}.mp4"

        # Create a temporary file with the list of input video files
        with open("Bjornulf/temp_video_list.txt", "w") as f:
            for _ in range(repetitions):
                f.write(f"file '{video_path}'\n")

        # Use ffmpeg to concatenate the video multiple times
        cmd = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', 'Bjornulf/temp_video_list.txt',
            '-c', 'copy',
            output_path
        ]
        subprocess.run(cmd, check=True)

        # Remove the temporary file
        os.remove("Bjornulf/temp_video_list.txt")

        print(f"Synced video saved to: {output_path}")
        return os.path.abspath(output_path)