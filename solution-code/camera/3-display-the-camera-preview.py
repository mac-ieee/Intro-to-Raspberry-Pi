###################################
# 3. Displaying the camera preview
###################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

camera.rotation = 0
camera.start_preview(alpha=200)
sleep(2)
camera.stop_preview()
