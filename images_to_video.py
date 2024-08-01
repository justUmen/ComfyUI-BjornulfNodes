import os
import numpy as np
import torch
import subprocess
from PIL import Image
import soundfile as sf
import glob

class imagesToVideo:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "fps": ("INT", {"default": 24, "min": 1, "max": 60}),
                "name_prefix": ("STRING", {"default": "output/imgs2video/me"}),
                "format": (["mp4", "webm"], {"default": "mp4"}),
                "mp4_encoder": (["libx264 (H.264)", "h264_nvenc (H.264 / NVIDIA GPU)", "libx265 (H.265)", "hevc_nvenc (H.265 / NVIDIA GPU)"], {"default": "h264_nvenc (H.264 / NVIDIA GPU)"}),
                "webm_encoder": (["libvpx-vp9", "libaom-av1 (VERY SLOW)"], {"default": "libvpx-vp9"}),
                "crf": ("INT", {"default": 19, "min": 0, "max": 63}),
                "force_transparency": ("BOOLEAN", {"default": False}),
                # "preset": (["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"], {"default": "medium"}),
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
    
    def image_to_video(self, images, fps, name_prefix, format, crf, force_transparency, mp4_encoder, webm_encoder, audio=None):
        # Remove any existing extension
        name_prefix = os.path.splitext(name_prefix)[0]
        
        # Find the next available number
        existing_files = glob.glob(f"{name_prefix}_*.{format}")
        if existing_files:
            max_num = max([int(f.split('_')[-1].split('.')[0]) for f in existing_files])
            next_num = max_num + 1
        else:
            next_num = 1
        
        # Create the new filename with the incremented number
        output_file = f"{name_prefix}_{next_num:04d}.{format}"
        
        temp_dir = "temp_images_imgs2video"
        # Clean up temp dir
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

        # Construct the FFmpeg command based on the selected format and encoder
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", os.path.join(temp_dir, "frame_%04d.png"),
        ]

        if temp_audio_file:
            ffmpeg_cmd.extend(["-i", temp_audio_file])

        if force_transparency:
            ffmpeg_cmd.extend([
                "-vf", "scale=iw:ih,format=rgba,split[s0][s1];[s0]lutrgb=r=0:g=0:b=0:a=0[transparent];[transparent][s1]overlay",
            ])

        if format == "mp4":
            if mp4_encoder == "h264_nvenc (H.264 / NVIDIA GPU)":
                mp4_encoder = "h264_nvenc"
                ffmpeg_cmd.extend([
                    "-c:v", mp4_encoder,
                    # "-preset", "p" + preset,  # NVENC uses different preset names
                    "-cq", str(crf),  # NVENC uses -cq instead of -crf
                ])
            if mp4_encoder == "hevc_nvenc (H.265 / NVIDIA GPU)":
                mp4_encoder = "hevc_nvenc"
                ffmpeg_cmd.extend([
                    "-c:v", mp4_encoder,
                    # "-preset", "p" + preset,  # NVENC uses different preset names
                    "-cq", str(crf),  # NVENC uses -cq instead of -crf
                ])
            elif mp4_encoder == "libx264":
                ffmpeg_cmd.extend([
                    "-c:v", mp4_encoder,
                    # "-preset", preset,
                    "-crf", str(crf),
                ])
            elif mp4_encoder == "libx265":
                ffmpeg_cmd.extend([
                    "-c:v", mp4_encoder,
                    # "-preset", preset,
                    "-crf", str(crf),
                    "-tag:v", "hvc1",  # For better compatibility
                ])
            ffmpeg_cmd.extend(["-pix_fmt", "yuv420p"]) #No transparency
            comment = """MP4 format : Widely compatible, efficient compression, No transparency support.
H.264: Fast encoding, widely compatible, larger file sizes for the same quality.
H.265: More efficient compression, smaller file sizes, better for high-resolution video, slower encoding, BUT less universal support."""
        elif format == "webm":
            if webm_encoder == "libvpx-vp9":
                # cpu_used = preset_to_cpu_used.get(preset, 3)  # Default to 3 if preset not found
                ffmpeg_cmd.extend([
                    "-c:v", webm_encoder,
                    # "-cpu-used", str(cpu_used),
                    "-deadline", "realtime",
                    "-crf", str(crf),
                    "-b:v", "0",
                    "-pix_fmt", "yuva420p", #Transparency
                ])
            elif webm_encoder == "libaom-av1 (VERY SLOW)":
                # cpu_used = preset_to_cpu_used.get(preset, 3)  # Default to 3 if preset not found
                webm_encoder = "libaom-av1"
                ffmpeg_cmd.extend([
                    "-c:v", webm_encoder,
                    # "-cpu-used", str(cpu_used),
                    "-deadline", "realtime",
                    "-crf", str(crf),
                    "-b:v", "0",
                    "-pix_fmt", "yuva420p", #Transparency
                ])
            comment = """WebM format: Supports transparency, open format, smaller file size, but less compatible than MP4."""

        if temp_audio_file:
            ffmpeg_cmd.extend(["-c:a", "libvorbis" if format == "webm" else "aac", "-shortest"])

        ffmpeg_cmd.append(output_file)

        # Run FFmpeg
        try:
            subprocess.run(ffmpeg_cmd, check=True)
            print(f"Video created successfully: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating video: {e}")
        finally:
            # Clean up temporary files
            # for file in os.listdir(temp_dir):
            #     os.remove(os.path.join(temp_dir, file))
            # os.rmdir(temp_dir)
            print("Temporary files not removed for debugging purposes.")

        return (comment,)