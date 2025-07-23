import pyautogui
import time

# Set the directory to save the screenshots
output_directory = "screenshots/"

# Define the screen resolution
screen_width, screen_height = pyautogui.size()

# Define the recording duration and interval
duration = 10  # 10 seconds
interval = 1  # 1 second

# Calculate the number of frames to capture
num_frames = int(duration / interval)

# Create the output directory if it doesn't exist
import os
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Capture and save screenshots
for i in range(num_frames):
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{output_directory}frame_{i:04d}.png")
    time.sleep(interval)
