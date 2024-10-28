import subprocess
from pathlib import Path
import os

class ConcatVideos:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_path_1": ("STRING", {"default": ""}),
                "video_path_2": ("STRING", {"default": ""}),
                "output_filename": ("STRING", {"default": "concatenated.mp4"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("concat_path",)
    FUNCTION = "concat_videos"
    OUTPUT_NODE = True
    CATEGORY = "Bjornulf"

    def __init__(self):
        # Get absolute paths for working directories
        self.work_dir = Path(os.path.abspath("temp_concat"))
        self.output_dir = Path(os.path.abspath("Bjornulf/concat_videos"))
        os.makedirs(self.work_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
    def concat_videos(self, video_path_1: str, video_path_2: str, output_filename: str):
        """
        Concatenate two videos using ffmpeg with high-quality settings.
        Returns the absolute path of the output file.
        """
        # Convert to absolute paths
        video_path_1 = os.path.abspath(video_path_1)
        video_path_2 = os.path.abspath(video_path_2)
        
        # Validate inputs
        if not (Path(video_path_1).exists() and Path(video_path_2).exists()):
            raise ValueError(f"Both video paths must exist.\nPath 1: {video_path_1}\nPath 2: {video_path_2}")
            
        # Create concat file with absolute paths
        concat_file = self.work_dir / "concat.txt"
        with open(concat_file, 'w') as f:
            f.write(f"file '{video_path_1}'\n")
            f.write(f"file '{video_path_2}'\n")
            
        # Set output path (absolute)
        output_path = self.output_dir / output_filename
        output_path = output_path.absolute()
        
        # Concatenate videos using ffmpeg with high quality settings
        cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', str(concat_file),
            # Video settings for maximum quality
            '-c:v', 'libx264',
            '-preset', 'veryslow',  # Slowest preset for best compression
            '-crf', '17',          # Lower CRF for higher quality (range: 0-51, 0 is lossless)
            '-x264-params', 'ref=6:me=umh:subme=7:trellis=2:direct-pred=auto:b-adapt=2',
            # Audio settings
            '-c:a', 'aac',
            '-b:a', '320k',        # High audio bitrate
            # Additional quality settings
            '-movflags', '+faststart',  # Enables streaming
            '-pix_fmt', 'yuv420p',      # Ensures compatibility
            str(output_path)
        ]
        
        try:
            # Run FFmpeg command
            process = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            
            # Return absolute path as string
            return (str(output_path),)
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFmpeg error: {e.stderr}")
        except Exception as e:
            raise RuntimeError(f"Error during video concatenation: {str(e)}")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")