#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  

import RPi.GPIO as GPIO
import time
import subprocess
import os

PIR_PIN = 11                    # GPIO11
GPIO.setmode(GPIO.BOARD)        # Use header pin numbers
GPIO.setup(PIR_PIN, GPIO.IN)

running = False         # Is a video currently playing?
player = "omxplayer"    # The video player being used
video_path = "/home/pi/video.mp4"   # Path to video file

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
                child = subprocess.Popen([player, video_path, opt])
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
