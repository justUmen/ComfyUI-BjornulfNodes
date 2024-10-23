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
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "video_path": ("STRING", {"default": ""}),
                "audio_duration": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 3600.0, "step": 0.001}),
            },
        }

    RETURN_TYPES = ("AUDIO", "STRING", "STRING", "FLOAT", "FLOAT", "INT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("sync_audio", "sync_audio_path", "sync_video_path", "video_fps", "video_duration", "sync_video_frame_count", "sync_audio_duration", "sync_video_duration")
    FUNCTION = "sync_audio_video"
    CATEGORY = "Bjornulf"

    def sync_audio_video(self, audio, video_path, audio_duration):
        if not isinstance(audio, dict) or 'waveform' not in audio or 'sample_rate' not in audio:
            raise ValueError("Expected audio input to be a dictionary with 'waveform' and 'sample_rate' keys")

        audio_data = audio['waveform']
        sample_rate = audio['sample_rate']

        # Get original video properties
        original_duration = self.get_video_duration(video_path)
        video_fps = self.get_video_fps(video_path)
        original_frame_count = self.get_frame_count(video_path)

        print(f"Original video duration: {original_duration}")
        print(f"Target audio duration: {audio_duration}")
        print(f"Video FPS: {video_fps}")
        print(f"Original frame count: {original_frame_count}")

        # Create synchronized versions of video and audio
        sync_video_path = self.create_sync_video(video_path, original_duration, audio_duration)
        sync_audio_path = self.save_audio(audio_data, sample_rate, audio_duration, original_duration)

        # Get properties of synchronized files
        sync_video_duration = self.get_video_duration(sync_video_path)
        sync_frame_count = self.get_frame_count(sync_video_path)
        sync_audio_duration = torchaudio.info(sync_audio_path).num_frames / sample_rate

        print(f"Sync video duration: {sync_video_duration}")
        print(f"Sync video frame count: {sync_frame_count}")
        print(f"Sync audio duration: {sync_audio_duration}")

        return (
            audio,  # Return original audio dictionary
            sync_audio_path,
            sync_video_path,
            video_fps,
            original_duration,
            sync_frame_count,
            sync_audio_duration,
            sync_video_duration
        )

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

    def get_frame_count(self, video_path):
        cmd = ['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_packets', '-of', 'csv=p=0', video_path]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return int(result.stdout.strip())

    def create_sync_video(self, video_path, original_duration, target_duration):
        os.makedirs("Bjornulf/sync_video", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        final_output_path = f"Bjornulf/sync_video/sync_video_{timestamp}.mp4"

        # Calculate the relative difference between durations
        duration_difference = abs(target_duration - original_duration) / original_duration

        # If target duration is longer but within 50% difference, use speed adjustment instead of repeating
        if target_duration > original_duration and duration_difference <= 0.5:
            # Calculate slowdown ratio
            speed_ratio = original_duration / target_duration
            pts_speed = 1/speed_ratio

            speed_adjust_cmd = [
                'ffmpeg',
                '-i', video_path,
                '-filter:v', f'setpts={pts_speed}*PTS',
                '-an',
                '-c:v', 'libx264',
                '-preset', 'medium',
                '-crf', '23',
                final_output_path
            ]
            subprocess.run(speed_adjust_cmd, check=True)
            print(f"Speed-adjusted video (slowdown ratio: {speed_ratio}) saved to: {final_output_path}")

        elif target_duration > original_duration:
            # Use the original repeating logic for larger differences
            repeat_count = math.ceil(target_duration / original_duration)
            concat_file = f"Bjornulf/sync_video/concat_{timestamp}.txt"
            with open(concat_file, 'w') as f:
                for _ in range(repeat_count):
                    f.write(f"file '{os.path.abspath(video_path)}'\n")

            concat_cmd = [
                'ffmpeg',
                '-f', 'concat',
                '-safe', '0',
                '-i', concat_file,
                '-c', 'copy',
                final_output_path
            ]
            subprocess.run(concat_cmd, check=True)
            os.remove(concat_file)
            print(f"Duplicated video {repeat_count} times, saved to: {final_output_path}")

        else:
            # Original speed-up logic remains the same
            speed_ratio = original_duration / target_duration
            
            if abs(speed_ratio - 1.0) <= 0.1:  # If the difference is less than 10%
                copy_cmd = [
                    'ffmpeg', '-i', video_path, '-c', 'copy', final_output_path
                ]
                subprocess.run(copy_cmd, check=True)
                print(f"Video copied without speed adjustment to: {final_output_path}")
            else:
                speed = min(speed_ratio, 1.5)
                pts_speed = 1/speed
                
                speed_adjust_cmd = [
                    'ffmpeg',
                    '-i', video_path,
                    '-filter:v', f'setpts={pts_speed}*PTS',
                    '-an',
                    '-c:v', 'libx264',
                    '-preset', 'medium',
                    '-crf', '23',
                    final_output_path
                ]
                subprocess.run(speed_adjust_cmd, check=True)
                print(f"Speed-adjusted video (ratio: {speed}) saved to: {final_output_path}")

        return os.path.abspath(final_output_path)

    def save_audio(self, audio_tensor, sample_rate, target_duration, original_video_duration):
        os.makedirs("Bjornulf/sync_audio", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Bjornulf/sync_audio/sync_audio_{timestamp}.wav"

        if audio_tensor.dim() == 3:
            audio_tensor = audio_tensor.squeeze(0)
        elif audio_tensor.dim() == 1:
            audio_tensor = audio_tensor.unsqueeze(0)

        current_duration = audio_tensor.shape[1] / sample_rate
        
        # Calculate the relative difference between durations
        duration_difference = abs(target_duration - original_video_duration) / original_video_duration

        # Calculate the final duration based on the same logic as create_sync_video
        if target_duration > original_video_duration:
            if duration_difference <= 0.5:
                # For small differences, we'll keep the original audio duration
                sync_video_duration = target_duration
            else:
                # For larger differences, we'll repeat the video
                sync_video_duration = math.ceil(target_duration / original_video_duration) * original_video_duration
        else:
            # Handle speed-up cases
            speed_ratio = original_video_duration / target_duration
            if abs(speed_ratio - 1.0) <= 0.1:
                sync_video_duration = original_video_duration
            else:
                speed = min(speed_ratio, 1.5)
                sync_video_duration = original_video_duration / speed

        # Adjust audio to match sync video duration
        if current_duration < sync_video_duration:
            # Pad with silence
            silence_samples = int((sync_video_duration - current_duration) * sample_rate)
            silence = torch.zeros(audio_tensor.shape[0], silence_samples)
            padded_audio = torch.cat([audio_tensor, silence], dim=1)
        else:
            # Trim audio to match sync video duration
            required_samples = int(sync_video_duration * sample_rate)
            padded_audio = audio_tensor[:, :required_samples]

        torchaudio.save(filename, padded_audio, sample_rate)
        print(f"target_duration: {target_duration}")
        print(f"original_video_duration: {original_video_duration}")
        print(f"sync_video_duration: {sync_video_duration}")
        print(f"current_audio_duration: {current_duration}")
        print(f"final_audio_duration: {padded_audio.shape[1] / sample_rate}")
        
        print(f"sync audio saved to: {filename}")
        return os.path.abspath(filename)