import os
import cv2
import numpy as np
import torch
from PIL import Image

class VideoToImagesList:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {"forceInput": True}),
                "frame_interval": ("INT", {"default": 1, "min": 1, "max": 100}),
                "max_frames": ("INT", {"default": 0, "min": 0, "max": 10000})
            }
        }
    
    RETURN_TYPES = ("IMAGE", "FLOAT", "FLOAT", "INT")
    RETURN_NAMES = ("IMAGE", "initial_fps", "new_fps", "total_frames")
    FUNCTION = "video_to_images"
    CATEGORY = "Bjornulf"

    def video_to_images(self, video_path, frame_interval=1, max_frames=0):
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        images = []
        
        # Get the initial fps of the video
        initial_fps = cap.get(cv2.CAP_PROP_FPS)
        
        # Get the total number of frames in the video
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        while True:
            ret, frame = cap.read()
            if not ret or (max_frames > 0 and len(images) >= max_frames):
                break
            
            if frame_count % frame_interval == 0:
                # Convert BGR to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(rgb_frame)
                
                # Convert PIL Image to tensor
                tensor_image = torch.from_numpy(np.array(pil_image).astype(np.float32) / 255.0).unsqueeze(0)
                images.append(tensor_image)
            
            frame_count += 1
        
        cap.release()
        
        if not images:
            raise ValueError("No frames were extracted from the video")
        
        # Calculate the new fps
        new_fps = initial_fps / frame_interval
        
        # Stack all images into a single tensor
        return (torch.cat(images, dim=0), initial_fps, new_fps, total_frames)
