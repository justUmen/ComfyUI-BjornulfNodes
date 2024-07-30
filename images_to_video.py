import os
import numpy as np
import torch
import subprocess
from PIL import Image
import soundfile as sf

class imagesToVideo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "fps": ("INT", {"default": 24, "min": 1, "max": 60}),
                "name_prefix": ("STRING", {"default": "output/imgs2video/me"}),
                "format": (["mp4", "webm"],),
                "crf": ("INT", {"default": 19, "min": 0, "max": 63}),
            },
            "optional": {
                "audio": ("AUDIO",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("comment",)
    FUNCTION = "image_to_video"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def image_to_video(self, images, fps, name_prefix, format, crf, audio=None):
        # Remove any existing extension
        name_prefix = os.path.splitext(name_prefix)[0]
        # Add the correct extension
        output_file = f"{name_prefix}.{format}"
        temp_dir = "temp_images_imgs2video"
        #Clean up temp dir
        if os.path.exists(temp_dir) and os.path.isdir(temp_dir):
            for file in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, file))
            os.rmdir(temp_dir)
        
        os.makedirs(temp_dir, exist_ok=True)
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else ".", exist_ok=True)

        # Save the tensor images as PNG files
        for i, img_tensor in enumerate(images):
            img = Image.fromarray((img_tensor.cpu().numpy() * 255).astype(np.uint8))
            if format == "webm":
                img = img.convert("RGBA")  # Ensure alpha channel for WebM
            img.save(os.path.join(temp_dir, f"frame_{i:04d}.png"))

        # Handle audio
        temp_audio_file = None
        if audio is not None:
            temp_audio_file = os.path.join(temp_dir, "temp_audio.wav")
            waveform = audio['waveform'].squeeze().numpy()
            sample_rate = audio['sample_rate']
            sf.write(temp_audio_file, waveform, sample_rate)

        # Construct the FFmpeg command based on the selected format
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", os.path.join(temp_dir, "frame_%04d.png"),
        ]

        if temp_audio_file:
            ffmpeg_cmd.extend(["-i", temp_audio_file])

        if format == "mp4":
            ffmpeg_cmd.extend([
                "-filter_complex", "[0:v]scale=iw:ih,format=rgba,split[s0][s1];[s0]lutrgb=r=0:g=0:b=0:a=0[transparent];[transparent][s1]overlay",
                "-crf", str(crf),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
            ])
            comment = "MP4 format: Widely compatible, efficient compression, no transparency support."
        elif format == "webm":
            # Fake transparency bug/feature with Inspyre.
            # Code to fix tat : creates a fully transparent background and then overlays your image on top of it, which forces the transparency to be preserved... wth is this guys?
            ffmpeg_cmd.extend([
                "-filter_complex", "[0:v]scale=iw:ih,format=rgba,split[s0][s1];[s0]lutrgb=r=0:g=0:b=0:a=0[transparent];[transparent][s1]overlay",
                "-c:v", "libvpx-vp9",
                "-pix_fmt", "yuva420p",
                "-b:v", "0",
                "-crf", str(crf),
                "-auto-alt-ref", "0",
            ])
            comment = "WebM format: Supports transparency, open format, smaller file size, but less compatible than MP4."

        if temp_audio_file:
            ffmpeg_cmd.extend(["-c:a", "libvorbis", "-shortest"])

        ffmpeg_cmd.append(output_file)

        # Run FFmpeg
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"Video created successfully: {output_file}")
        except subprocess.CalledProcessCode as e:
            print(f"Error creating video: {e}")
        finally:
            # Clean up temporary files
            # for file in os.listdir(temp_dir):
            #     os.remove(os.path.join(temp_dir, file))
            # os.rmdir(temp_dir)
            print("Temporary files not removed for debugging purposes.")

        return (comment,)