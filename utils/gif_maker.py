from moviepy.editor import VideoFileClip

import imageio
import os
from moviepy.editor import *

def convert_to_gif(video_path, gif_path, loop=True):
    video = VideoFileClip(video_path)
    if loop:
        duration = video.duration
        video = concatenate_videoclips([video] * int(duration / video.duration))
    video.write_gif(gif_path, fps=10)

# Example usage:
video_path = "videos/seg_video.mp4"  # Path to your input video
gif_path = "seg_gif.gif"  # Path to save the output GIF
convert_to_gif(video_path, gif_path)