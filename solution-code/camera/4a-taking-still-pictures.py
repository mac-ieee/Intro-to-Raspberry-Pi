###################################
# 4.a Taking still pictures
###################################
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

camera.rotation = 0
camera.start_preview(alpha=200)
camera.rotation = 180
sleep(2)
camera.capture('./stillpic.jpg')
camera.stop_preview()
