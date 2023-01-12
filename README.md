# ytd-bot

This is a script that automates the process of downloading a video from YouTube, adding an advertisement to the video, uploading the modified video to a specified YouTube channel, and saving the video's information to a local database.

## Requirements

Python 3.x
pytube
moviepy
selenium
undetected_chromedriver

## Usage

Clone the repository and navigate to the project's root directory.
Install the required packages by running pip install -r requirements.txt
Run the script by executing python main.py in the terminal

## Configuration

url : set the url of the video you want to download
input_file_path : the path of the downloaded video
output_file_path : the path of the video after adding the advertisement
gif_clip : the path of the advertisement video
upload_url : the url of the YouTube Studio page where you want to upload the video
profile_path : the path of the chrome profile you want to use
Additional information
The script uses a selenium webdriver to interact with the YouTube Studio page, so you must have the chrome browser installed.
You need to sign in to your YouTube account before running the script, as the script will use the cookies stored in the profile.
The script uses the Database class to save the video information to a local SQLite database.
The VideoDownloader class is responsible for downloading the video from YouTube.
The functions module contains helper functions used throughout the script.
The script will print the progress of the video download, video processing, and video upload.
It will also print the counter of the while loop in case it takes more than 10 minutes to upload the video.

Once the video is uploaded, the script will print "Video uploaded" and add the url, the title, and the description to the database.
