from pytube import YouTube
from helpers import Database
from helpers import VideoDownloader
from helpers import GetLatestFile
import helpers.functions as f
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from moviepy.editor import VideoFileClip, CompositeVideoClip

# Constants
# Get the last modified file
input_file_path = f.get_file_path("input-videos")
output_file_path = f.get_file_path("output-videos")

# Set the URL of the video
url = "https://youtu.be/CbpKDYg9Qvo"
# Create an instance of the Database class
db = Database("data.db")

# Check the items in the database§
url = db.check_url(url)

# Print the new list of items
print(url)

# check if the url is not Exists
if url is not None:
    # Create an instance of the VideoDownloader class
    d = VideoDownloader(url, output_path="input-videos")
    # Download the video
    print("Downloading video ...")
    d.download()
    vid_title = d.vid_title()
    input_file_path = f.get_file_path("input-videos")
else:
    raise Exception("Video already downloaded")


# Load the input video
input_video = VideoFileClip(input_file_path)

# Load the GIF file as a video clip
gif_clip = VideoFileClip("ads/gif.mp4")
gif_clip = gif_clip.set_duration(input_video.duration)

# Scale the GIF clip to a smaller size
gif_clip = gif_clip.resize(width=input_video.w)

# Set the position of the GIF clip
gif_clip = gif_clip.set_pos((0, 0))

# Combine the input video and the GIF clip
output_video = CompositeVideoClip([input_video, gif_clip])

# Save the output video
output_video.write_videofile("output-videos/" + vid_title + ".mp4", fps=30)

output_file_path = f.get_file_path("output-videos")


# Selenium
print("Starting Selenium")
profile_path = "/Users/bashir/Library/Application Support/Google/Chrome/myprofile"
options = uc.ChromeOptions()
options.user_data_dir = profile_path
driver = uc.Chrome(options=options, version_main=108)
upload_url = "https://studio.youtube.com/channel/UCH4fTtYeGAfwgV3Gct0Nt9g/videos?d=ud"
driver.get(upload_url)

# upload_loc
f.locate(By.XPATH, "//input[@type='file']", driver).send_keys(
    "/Users/bashir/Projects/ytd-bot/" + output_file_path
)

# title_loc
f.locate(By.ID, "textbox", driver).send_keys(f.name_clean(vid_title))
# next
f.locate(By.ID, "next-button", driver).click()
sleep(1)
# next
f.locate(By.ID, "next-button", driver).click()
sleep(1)
# next
f.locate(By.ID, "next-button", driver).click()
sleep(1)
# next
f.locate(By.ID, "done-button", driver).click()
sleep(1)


print("Uploading Video ...")
video_uploading = f.locate(By.ID, "dialog-title", driver).text

print("Uploading Video ...")
counter = 0
while True:
    if "processing" in video_uploading:
        print("Video uploaded")
        break
    elif counter >= 10:
        print("Video not sure uploaded")
        break
    else:
        sleep(60)
        print(counter)
        counter += 1
        video_uploading = f.locate(By.ID, "dialog-title", driver).text

print("Done")

# Add the url to the database
db.add_url(url)
db.close()
driver.quit()
print("Done")
