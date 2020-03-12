##############################
# 6. Mini-project: DIY Camera
##############################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

camera = PiCamera()

GPIO.setmode(GPIO.BOARD)
capturePin = 12
GPIO.setup(capturePin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(12) == 0:
        camera.start_preview(alpha=200)
        sleep(2)
        camera.capture('./diycamera.jpg')
        camera.stop_preview()
