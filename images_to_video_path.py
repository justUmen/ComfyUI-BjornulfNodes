import os
import uuid
import subprocess
import tempfile
import torch
import numpy as np
from PIL import Image
import wave

class ImagesListToVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "frames_per_second": ("FLOAT", {"default": 30, "min": 1, "max": 120, "step": 1}),
            },
            "optional": {
                "audio_path": ("STRING", {"default": "", "multiline": False}),
                "audio": ("AUDIO", {"default": None}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video_path",)
    FUNCTION = "images_to_video"
    CATEGORY = "Bjornulf"

    def images_to_video(self, images, frames_per_second=30, audio_path="", audio=None):
        # Create the output directory if it doesn't exist
        output_dir = os.path.join("Bjornulf", "images_to_video")
        os.makedirs(output_dir, exist_ok=True)

        # Generate a unique filename for the video
        video_filename = f"video_{uuid.uuid4().hex}.mp4"
        video_path = os.path.join(output_dir, video_filename)

        # Create a temporary directory to store image files and audio
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save each image as a PNG file in the temporary directory
            for i, img in enumerate(images):
                img_np = self.convert_to_numpy(img)
                if img_np.shape[-1] != 3:
                    img_np = self.convert_to_rgb(img_np)
                img_pil = Image.fromarray(img_np)
                img_path = os.path.join(temp_dir, f"frame_{i:05d}.png")
                img_pil.save(img_path)

            # Prepare FFmpeg command
            ffmpeg_cmd = [
                "ffmpeg",
                "-framerate", str(frames_per_second),
                "-i", os.path.join(temp_dir, "frame_%05d.png"),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-crf", "19"
            ]

            # Handle audio
            temp_audio_path = None
            if audio is not None and isinstance(audio, dict):
                waveform = audio['waveform'].numpy().squeeze()
                sample_rate = audio['sample_rate']
                temp_audio_path = os.path.join(temp_dir, "temp_audio.wav")
                self.write_wav(temp_audio_path, waveform, sample_rate)
            elif audio_path and os.path.isfile(audio_path):
                temp_audio_path = audio_path

            if temp_audio_path:
                # Create temporary video without audio first
                temp_video = os.path.join(temp_dir, "temp_video.mp4")
                temp_cmd = ffmpeg_cmd + ["-y", temp_video]
                
                try:
                    # Create video without audio
                    subprocess.run(temp_cmd, check=True, capture_output=True, text=True)
                    
                    # Add audio to the video
                    audio_cmd = [
                        "ffmpeg",
                        "-i", temp_video,
                        "-i", temp_audio_path,
                        "-c:v", "copy",
                        "-c:a", "aac",
                        "-shortest",
                        "-y",
                        video_path
                    ]
                    subprocess.run(audio_cmd, check=True, capture_output=True, text=True)
                except subprocess.CalledProcessError as e:
                    print(f"FFmpeg error: {e.stderr}")
                    return ("",)
            else:
                # No audio, just create the video directly
                ffmpeg_cmd.append("-y")
                ffmpeg_cmd.append(video_path)
                try:
                    subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
                except subprocess.CalledProcessError as e:
                    print(f"FFmpeg error: {e.stderr}")
                    return ("",)

        return (video_path,)

    def write_wav(self, file_path, audio_data, sample_rate):
        with wave.open(file_path, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 2 bytes per sample
            wav_file.setframerate(sample_rate)
            
            # Normalize and convert to 16-bit PCM
            audio_data = np.int16(audio_data * 32767)
            
            # Write audio data
            wav_file.writeframes(audio_data.tobytes())

    def convert_to_numpy(self, img):
        if isinstance(img, torch.Tensor):
            img = img.cpu().numpy()
        if img.dtype == np.uint8:
            return img
        elif img.dtype == np.float32 or img.dtype == np.float64:
            return (img * 255).astype(np.uint8)
        else:
            raise ValueError(f"Unsupported data type: {img.dtype}")

    def convert_to_rgb(self, img):
        if img.shape[-1] == 1:  # Grayscale
            return np.repeat(img, 3, axis=-1)
        elif img.shape[-1] == 768:  # Latent space representation
            # This is a placeholder. You might need a more sophisticated method to convert latent space to RGB
            img = img.reshape((-1, 3))  # Reshape to (H*W, 3)
            img = (img - img.min()) / (img.max() - img.min())  # Normalize to [0, 1]
            img = (img * 255).astype(np.uint8)
            return img.reshape((img.shape[0], -1, 3))  # Reshape back to (H, W, 3)
        elif len(img.shape) == 2:  # 2D array
            return np.stack([img, img, img], axis=-1)
        else:
            raise ValueError(f"Unsupported image shape: {img.shape}")