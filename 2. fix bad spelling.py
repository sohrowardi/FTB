import os
import random
import nltk
from moviepy.editor import VideoFileClip

# Download NLTK resources
nltk.download('punkt')

# Function to calculate similarity between two strings using NLTK's edit distance
def similarity(string1, string2):
    edit_distance = nltk.edit_distance(string1, string2)
    max_len = max(len(string1), len(string2))
    return 1 - (edit_distance / max_len)

# Folder containing clips (relative path)
clip_folder = "clips"

# List all files in the folder
clip_files = [f for f in os.listdir(clip_folder) if os.path.isfile(os.path.join(clip_folder, f))]

# Continuously ask for user input
while True:
    user_input = input("Enter a phrase: ").lower()  # Convert input to lowercase for case-insensitivity
    
    # Find the clip filenames with the highest similarity to the user input
    max_similarity = -1
    matching_clips = []
    for clip in clip_files:
        sim = similarity(user_input, clip.lower())
        if sim > max_similarity:
            max_similarity = sim
            matching_clips = [clip]
        elif sim == max_similarity:
            matching_clips.append(clip)
    
    # If no matching clips found, inform the user
    if not matching_clips:
        print("No matching clips found.")
        continue
    
    # Randomly select one of the matching clips
    random_clip = random.choice(matching_clips)
    print(f"Playing: {random_clip}")
    
    # Load the video using moviepy
    video_path = os.path.join(clip_folder, random_clip)
    clip = VideoFileClip(video_path)
    
    # Play the video
    clip.preview()
    
    # Close the video preview window
    clip.close()

#worked