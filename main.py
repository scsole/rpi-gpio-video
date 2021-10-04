#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  

from genericpath import exists
import RPi.GPIO as GPIO
import time
import subprocess
import os

PIR_PIN = 11                    # GPIO11
GPIO.setmode(GPIO.BOARD)        # Use header pin numbers
GPIO.setup(PIR_PIN, GPIO.IN)

running = False         # Is a video currently playing?
player = "omxplayer"    # The video player being used
primary_video_path = "/mnt/usb/video.mp4"   # Path to primary video file
secondary_video_path = "/home/pi/video.mp4" # Path to backup video file
video_path = primary_video_path

child = 0

if player == "vlc":
    opt = '--play-and-exit'
else:
    opt = ''

try:
    print("Waiting for motion")

    while True:
        if not GPIO.input(PIR_PIN):
            if running == False:
                print("Motion detected")
                if os.path.exists(primary_video_path):
                    video_path = primary_video_path
                elif os.path.exists(secondary_video_path):
                    video_path = secondary_video_path
                    print("INFO: Using secondary video")
                else:
                    print("WARN: Video files not accessible, ignoring motion")
                    continue
                child = subprocess.Popen([player, '-o', 'local', video_path, opt])
                running = True
                print("Playing video")

        if running == True:
            child.poll()
            if child.returncode == 0:
                running = False
                print("Video complete, waiting for motion")
            time.sleep(1)

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
