import re
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from moviepy.editor import VideoFileClip, CompositeVideoClip


# Regex
def name_clean(string):
    return re.sub(r"[^\x00-\uFFFF]", "", string)


# Get file path
def get_file_path(dir_path):
    # Get all files in the directory
    files = os.listdir(dir_path)
    # Get the last modified file
    try:
        latest_file = max(
            files, key=lambda x: os.path.getctime(os.path.join(dir_path, x))
        )
    except ValueError:
        print("No files in the directory")
        return None
    return os.path.join(dir_path, latest_file)


# Locate element
def locate(by, value, driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except Exception as e:
        print(f"Error: {e}. Retrying...")
        sleep(1)
        locate(by, value, driver)
