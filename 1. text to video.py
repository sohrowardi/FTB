import os
import random
from moviepy.editor import VideoFileClip

# Folder containing clips (relative path)
clip_folder = "clips"

# List all files in the folder
clip_files = [f for f in os.listdir(clip_folder) if os.path.isfile(os.path.join(clip_folder, f))]

# Continuously ask for user input
while True:
    user_input = input("Enter a phrase: ").lower()  # Convert input to lowercase for case-insensitivity
    matching_clips = [clip for clip in clip_files if user_input in clip.lower()]
    if matching_clips:
        random_clip = random.choice(matching_clips)
        print(f"Playing: {random_clip}")
        video_path = os.path.join(clip_folder, random_clip)
        clip = VideoFileClip(video_path)
        clip.preview()
        clip.close()
    else:
        print("No matching clip found.")


#worked