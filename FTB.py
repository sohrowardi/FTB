import os
import random
import nltk
from moviepy.editor import VideoFileClip
from tkinter import Tk, filedialog

# Download NLTK resources
nltk.download('punkt')

# Function to calculate similarity between two strings using NLTK's edit distance
def similarity(string1, string2):
    edit_distance = nltk.edit_distance(string1, string2)
    max_len = max(len(string1), len(string2))
    return 1 - (edit_distance / max_len)

# Function to select a folder using a file dialog if .clips folder doesn't exist or is empty
def select_folder():
    Tk().withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory(title="Select the Clip Folder")
    return folder_selected

# Folder containing clips (relative path)
clip_folder = ".clips"

# Check if the folder exists and contains clips
if not os.path.exists(clip_folder) or not os.listdir(clip_folder):
    print(f"'{clip_folder}' folder doesn't exist or is empty. Please select a clip folder.")
    clip_folder = select_folder()

# List all files in the selected folder
clip_files = [f for f in os.listdir(clip_folder) if os.path.isfile(os.path.join(clip_folder, f))]

if not clip_files:
    print(f"No clips found in the folder: {clip_folder}")
    exit()

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