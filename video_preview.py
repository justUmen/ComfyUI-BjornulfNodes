import os
import shutil
# import logging

class VideoPreview:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_path": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "preview_video"
    CATEGORY = "Bjornulf"
    OUTPUT_NODE = True

    def preview_video(self, video_path):
        if not video_path:
            return {"ui": {"error": "No video path provided."}}

        # Keep the "output" folder structure for copying
        dest_dir = os.path.join("output", "Bjornulf", "preview_video")
        os.makedirs(dest_dir, exist_ok=True)
        
        video_name = os.path.basename(video_path)
        dest_path = os.path.join(dest_dir, video_name)
        
        if os.path.abspath(video_path) != os.path.abspath(dest_path):
            shutil.copy2(video_path, dest_path)
            print(f"Video copied successfully to {dest_path}")
        else:
            print(f"Video is already in the destination folder: {dest_path}")

        # Determine the video type based on file extension
        _, file_extension = os.path.splitext(dest_path)
        video_type = file_extension.lower()[1:]  # Remove the dot from extension

        # logging.info(f"Video type: {video_type}")
        # logging.info(f"Video path: {dest_path}")
        # logging.info(f"Destination directory: {dest_dir}")
        # logging.info(f"Video name: {video_name}")

        # Create a new variable for the return value without "output"
        return_dest_dir = os.path.join("Bjornulf", "preview_video")

        # Return the video name and the modified destination directory
        return {"ui": {"video": [video_name, return_dest_dir]}}
