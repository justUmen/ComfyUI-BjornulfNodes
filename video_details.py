import subprocess
import json
from pathlib import Path
import os
import re
try:
    import ffmpeg
    FFMPEG_PYTHON_AVAILABLE = True
except ImportError:
    FFMPEG_PYTHON_AVAILABLE = False

class VideoDetails:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_path": ("STRING", {"default": "", "forceInput": True}),
                "ffprobe_path": ("STRING", {"default": "ffprobe"}),
                "use_python_ffmpeg": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT", "FLOAT", "INT", "INT", "STRING", "STRING", 
                    "STRING", "STRING", "STRING", "STRING", "FLOAT", "STRING", "STRING")
    RETURN_NAMES = ("filename", "video_path", "width", "height", "fps", "total_frames", "duration_seconds",
                   "video_codec", "video_bitrate", "pixel_format",
                   "audio_codec", "audio_bitrate", "container_format",
                   "duration_seconds_float", "full_info", "FFMPEG_CONFIG_JSON")
    FUNCTION = "get_video_info"
    CATEGORY = "Bjornulf"

    def extract_bitrate(self, text):
        """Extract bitrate value from text."""
        match = re.search(r'(\d+(?:\.\d+)?)\s*(?:kb/s|Kb/s|KB/s|Mb/s|MB/s)', text)
        if match:
            value = float(match.group(1))
            if 'mb/s' in text.lower() or 'MB/s' in text:
                value *= 1000
            return f"{value:.0f}k"
        return "N/A"

    def create_json_output(self, filename, video_path, width, height, fps, total_frames,
                         duration_seconds, duration_seconds_float, video_codec,
                         video_bitrate, pixel_format, audio_codec, audio_bitrate,
                         container_format):
        """Create a JSON string containing all video information in FFmpegConfig format."""
        video_info = {
            "ffmpeg": {
                "path": "ffmpeg",  # Default value since this is from probe
                # "use_python_ffmpeg": False  # Default value since this is from probe
            },
            "video": {
                "codec": video_codec if video_codec != "N/A" else "None",
                "bitrate": video_bitrate if video_bitrate != "N/A" else "0k",
                "preset": "None",  # Not available from probe
                "pixel_format": pixel_format if pixel_format != "N/A" else "None",
                "crf": 0,  # Not available from probe
                "resolution": {
                    "width": width,
                    "height": height
                },
                "fps": {
                    "force_fps": fps,
                    "enabled": False  # This is source fps, not forced
                }
            },
            "audio": {
                "enabled": audio_codec != "N/A" and audio_codec != "None",
                "codec": audio_codec if audio_codec != "N/A" else "None",
                "bitrate": audio_bitrate if audio_bitrate != "N/A" else "0k"
            },
            "output": {
                "container_format": container_format if container_format != "N/A" else "None"
            }
        }
        return json.dumps(video_info, indent=2)

    def create_full_info_string(self, video_path, width, height, fps, total_frames,
                              duration_seconds, duration_seconds_float, video_codec,
                              video_bitrate, pixel_format, audio_codec, audio_bitrate,
                              container_format):
        return f"""Video Information:
Filename: {os.path.basename(video_path)}
Resolution: {width}x{height}
FPS: {fps:.3f}
Total Frames: {total_frames}
Duration: {duration_seconds} seconds ({duration_seconds_float:.3f})
Video Codec: {video_codec}
Video Bitrate: {video_bitrate}
Pixel Format: {pixel_format}
Audio Codec: {audio_codec}
Audio Bitrate: {audio_bitrate}
Container Format: {container_format}
"""

    def get_video_info_python_ffmpeg(self, video_path):
        """Get video info using python-ffmpeg."""
        if not FFMPEG_PYTHON_AVAILABLE:
            raise RuntimeError("python-ffmpeg is not installed. Please install it with 'pip install ffmpeg-python'")

        try:
            probe = ffmpeg.probe(video_path)
            
            # Initialize variables with default values
            width = 0
            height = 0
            fps = 0.0
            total_frames = 0
            duration_seconds = 0
            duration_seconds_float = 0.0
            video_codec = "N/A"
            video_bitrate = "N/A"
            pixel_format = "N/A"
            audio_codec = "N/A"
            audio_bitrate = "N/A"
            container_format = "N/A"

            # Extract format information
            format_data = probe['format']

            container_format = format_data.get('format_name', "N/A").split(',')[0]

            # With:
            format_name = format_data.get('format_name', "N/A")
            if 'mp4' in format_name.lower():
                container_format = 'mp4'
            else:
                container_format = format_name.split(',')[0]

            duration_seconds_float = float(format_data.get('duration', 0))
            duration_seconds = int(duration_seconds_float)

            # Process streams
            for stream in probe['streams']:
                if stream['codec_type'] == 'video':
                    width = int(stream.get('width', 0))
                    height = int(stream.get('height', 0))
                    
                    fps_str = stream.get('r_frame_rate', '')
                    if fps_str and fps_str != '0/0':
                        num, den = map(int, fps_str.split('/'))
                        fps = num / den if den != 0 else 0.0
                    
                    total_frames = int(stream.get('nb_frames', 0))
                    if total_frames == 0 and fps > 0 and duration_seconds_float > 0:
                        total_frames = int(duration_seconds_float * fps)
                    
                    video_codec = stream.get('codec_name', "N/A")
                    pixel_format = stream.get('pix_fmt', "N/A")
                    video_bitrate = f"{int(int(stream.get('bit_rate', 0))/1000)}k"
                    
                elif stream['codec_type'] == 'audio':
                    audio_codec = stream.get('codec_name', "N/A")
                    audio_bitrate = stream.get('bit_rate', "N/A")
                    if audio_bitrate != "N/A":
                        audio_bitrate = f"{int(int(audio_bitrate)/1000)}k"

            filename = os.path.basename(video_path)
            
            # Create full info string and JSON outputs
            full_info = self.create_full_info_string(
                video_path, width, height, fps, total_frames,
                duration_seconds, duration_seconds_float, video_codec,
                video_bitrate, pixel_format, audio_codec, audio_bitrate,
                container_format
            )
            
            full_info_json = self.create_json_output(
                filename, video_path, width, height, fps, total_frames,
                duration_seconds, duration_seconds_float, video_codec,
                video_bitrate, pixel_format, audio_codec, audio_bitrate,
                container_format
            )

            return (
                filename,
                video_path,
                width,
                height,
                fps,
                total_frames,
                duration_seconds,
                video_codec,
                video_bitrate,
                pixel_format,
                audio_codec,
                audio_bitrate,
                container_format,
                duration_seconds_float,
                full_info,
                full_info_json
            )

        except Exception as e:
            raise RuntimeError(f"Error analyzing video with python-ffmpeg: {str(e)}")

    def get_video_info(self, video_path: str, ffprobe_path: str, use_python_ffmpeg: bool):
        """Get detailed information about a video file."""
        video_path = os.path.abspath(video_path)
        if not os.path.exists(video_path):
            raise ValueError(f"Video file not found: {video_path}")

        if use_python_ffmpeg:
            return self.get_video_info_python_ffmpeg(video_path)

        # Original ffmpeg/ffprobe implementation
        probe_cmd = [
            ffprobe_path,
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            video_path
        ]

        info_cmd = [
            ffprobe_path,
            '-i', video_path,
            '-hide_banner'
        ]

        try:
            probe_result = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            probe_data = json.loads(probe_result.stdout)
            
            info_result = subprocess.run(info_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            ffmpeg_output = info_result.stderr

            # Initialize variables with default values
            width = 0
            height = 0
            fps = 0.0
            total_frames = 0
            duration_seconds = 0
            duration_seconds_float = 0.0
            video_codec = "N/A"
            video_bitrate = "N/A"
            pixel_format = "N/A"
            audio_codec = "N/A"
            audio_bitrate = "N/A"
            container_format = "N/A"

            # Extract information from probe data
            if 'format' in probe_data:
                format_data = probe_data['format']
                # container_format = format_data.get('format_name', "N/A").split(',')[0]
                container_format = format_data.get('format_name', "N/A").split(',')[0]
                # With:
                format_name = format_data.get('format_name', "N/A")
                if 'mp4' in format_name.lower():
                    container_format = 'mp4'
                else:
                    container_format = format_name.split(',')[0]
                duration_seconds_float = float(format_data.get('duration', 0))
                duration_seconds = int(duration_seconds_float)

            # Process streams
            for stream in probe_data.get('streams', []):
                if stream['codec_type'] == 'video':
                    width = int(stream.get('width', 0))
                    height = int(stream.get('height', 0))
                    
                    fps_str = stream.get('r_frame_rate', '')
                    if fps_str and fps_str != '0/0':
                        num, den = map(int, fps_str.split('/'))
                        fps = num / den if den != 0 else 0.0
                    
                    total_frames = int(stream.get('nb_frames', 0))
                    if total_frames == 0 and fps > 0 and duration_seconds_float > 0:
                        total_frames = int(duration_seconds_float * fps)
                    
                    video_codec = stream.get('codec_name', "N/A")
                    pixel_format = stream.get('pix_fmt', "N/A")
                    
                elif stream['codec_type'] == 'audio':
                    audio_codec = stream.get('codec_name', "N/A")
                    audio_bitrate = stream.get('bit_rate', "N/A")
                    if audio_bitrate != "N/A":
                        audio_bitrate = f"{int(int(audio_bitrate)/1000)}k"

            # Extract video bitrate from ffmpeg output
            video_bitrate = self.extract_bitrate(ffmpeg_output)

            filename = os.path.basename(video_path)

            # Create full info string
            full_info = self.create_full_info_string(
                video_path, width, height, fps, total_frames,
                duration_seconds, duration_seconds_float, video_codec,
                video_bitrate, pixel_format, audio_codec, audio_bitrate,
                container_format
            )

            # Create JSON output
            full_info_json = self.create_json_output(
                filename, video_path, width, height, fps, total_frames,
                duration_seconds, duration_seconds_float, video_codec,
                video_bitrate, pixel_format, audio_codec, audio_bitrate,
                container_format
            )

            return (
                filename,
                video_path,
                width,
                height,
                fps,
                total_frames,
                duration_seconds,
                video_codec,
                video_bitrate,
                pixel_format,
                audio_codec,
                audio_bitrate,
                container_format,
                duration_seconds_float,
                full_info,
                full_info_json
            )

        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error running ffmpeg/ffprobe: {e.stderr}")
        except json.JSONDecodeError:
            raise RuntimeError("Error parsing ffprobe output")
        except Exception as e:
            raise RuntimeError(f"Error analyzing video: {str(e)}")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")