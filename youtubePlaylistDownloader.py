import os
from pytube import Playlist

# Function to create a folder if it doesn't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name

# Function to sanitize video title
def sanitize_title(title):
    return "".join([c if c.isalnum() or c in ' ._-' else '_' for c in title])

# Ask the user for the playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")

# Create a Playlist object
playlist = Playlist(playlist_url)

# Ask the user for the folder name
folder_name = input("Enter the name of the folder to save the videos: ")

# Create the folder
folder_path = create_folder(folder_name)

# Loop through all videos in the playlist
for index, video in enumerate(playlist.videos, start=1):
    # Get the title of the video
    video_title = video.title
    # Sanitize the video title to use it as a filename
    safe_title = sanitize_title(video_title)
    # Format the prefix with leading zeros (e.g., 001, 002, ...)
    prefix = f"{index:03}_"
    # Set the output file path
    output_filename = f"{prefix}{safe_title}.mp4"
    output_path = os.path.join(folder_path, output_filename)
    
    # Check if the file already exists
    if os.path.exists(output_path):
        print(f"Skipping {video_title}, already downloaded as {output_filename}")
        continue
    
    print(f"Downloading {video_title} as {output_filename}...")
    # Download the video in the highest available resolution
    video.streams.get_highest_resolution().download(output_path=folder_path, filename=output_filename)
    print(f"Downloaded {video_title} to {output_path}")

print(f"All videos have been downloaded to the folder: {folder_path}")
