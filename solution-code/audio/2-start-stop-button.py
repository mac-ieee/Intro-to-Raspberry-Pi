#############################
#   Playing an mp3 file
#   using start and stop
#   buttons.
############################

import os 
from time import sleep 
import RPi.GPIO as GPIO 


GPIO.setmode(GPIO.BOARD) 
start = 18 # “start” button connects to pin 18 
stop = 16 # “stop” button connects to pin 16 

# Initialize the input pins 
GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

song = 'mpg123 -q name.mp3 &' # replace “name.mp3” with filename 
playing = 0 # flag keeps track of whether a song is playing 

while True: 
    if (GPIO.input(start) == 0 and playing == 0): # start pressed 
        os.system(song) # play the mp3 file 
        playing = 1 # raise the playing flag 
        print('Now Playing: ', song(10:-2)) 
    
    if (GPIO.input(stop) == 0): 
        os.system('pkill mpg123') # stop playing the file 
        playing = 0 # reset the flag to zero 
        print('The song was stopped') 
        sleep(0.2) 
        
GPIO.cleanup()