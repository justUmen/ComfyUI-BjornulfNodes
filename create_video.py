import os
import numpy as np
import torch
import subprocess
from PIL import Image

class imgs2vid:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "fps": ("INT", {"default": 30, "min": 1, "max": 60}),
                "video_name_NO_format": ("STRING", {"default": "output"}),
                "format": (["mp4", "webm"],),
                "audio_path": ("STRING", {"default": "/home/umen/6sec.wav"}),  # New audio input
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("comment",)
    FUNCTION = "create_video"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def create_video(self, images, fps, video_name_NO_format, format, audio_path):
        # Remove any existing extension
        video_name_NO_format = os.path.splitext(video_name_NO_format)[0]
        # Add the correct extension
        output_file = f"{video_name_NO_format}.{format}"
        temp_dir = "temp_images"
        os.makedirs(temp_dir, exist_ok=True)
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)

        # Save the tensor images as PNG files
        for i, img_tensor in enumerate(images):
            img = Image.fromarray((img_tensor.cpu().numpy() * 255).astype(np.uint8))
            if format == "webm":
                img = img.convert("RGBA")  # Ensure alpha channel for WebM
            img.save(os.path.join(temp_dir, f"frame_{i:04d}.png"))

        # Construct the FFmpeg command based on the selected format
        if format == "mp4":
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",
                "-framerate", str(fps),
                "-i", os.path.join(temp_dir, "frame_%04d.png"),
                "-i", str(audio_path),
                "-crf", "19",
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                output_file
            ]
            comment = "MP4 format: Widely compatible, efficient compression, no transparency support."
        elif format == "webm":
            ffmpeg_cmd = [
                "ffmpeg",
                "-y",
                "-framerate", str(fps),
                "-i", os.path.join(temp_dir, "frame_%04d.png"),
                "-i", str(audio_path),
                "-crf", "19",
                "-c:v", "libvpx",
                "-b:v", "1M",  # Set video bitrate
                "-auto-alt-ref", "0",  # Disable auto alt ref
                "-c:a", "libvorbis",
                "-pix_fmt", "yuva420p",
                "-shortest",
                output_file
            ]
            comment = "WebM format: Supports transparency, open format, smaller file size, but less compatible than MP4."

        # Run FFmpeg
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"Video created successfully: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating video: {e}")
        finally:
            # Clean up temporary files
            for file in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, file))
            os.rmdir(temp_dir)

        return (comment,)

# Example usage
# images = [torch.rand(256, 256, 3) for _ in range(10)]  # Replace with actual image tensors
# imgs2vid().create_video(images, 30, "output", "webm", "/home/
