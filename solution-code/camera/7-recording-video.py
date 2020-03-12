#####################
# 7. Recording Video
#####################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

camera.start_preview()
camera.start_recording('./testvideo.h264')
sleep(9)
camera.stop_recording()
camera.stop_preview()
