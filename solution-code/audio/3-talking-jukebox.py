#############################
#   Recreating a 
#   talking jukebox.
############################

import os 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

start = 16
skip = 18
skip_p = 22

GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(skip, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(skip_p, GPIO.IN, pull_up_down=GPIO.PUD_UP)

playing = False
songs = ['rickroll', 'staying_alive', 'careless', 'cant_touch_this']
index = 0

while True: #continuously check for button presses

    #if start button pressed 
    if GPIO.input(start)==0:
        print("Pressed Play/Pause")
        if playing == False:
            song = 'mpg123 -q ' + songs[index] + '.mp3 &'
            print("now playing song "+ songs[index])
            os.system("echo 'playing song" + songs[index]+ "' | festival --tts")
            os.system(song)
            playing = True
        else:
            os.system('pkill mpg123')
            print("Stopped playing.")
            playing = False

        sleep(1)  #pause in order to debounce buttons

    #if skip button is pressed
    if GPIO.input(skip)==0:
        print("Pressed skip to next")
        #move index to next song, or back to start
        if index < len(songs)-1:
            index = index + 1
        else:
            index = 0

        if playing = True:
            os.system('pkill mpg123')
            playing = False
            song = 'mpg123 -q ' + songs[index] + '.mp3 &'
            os.system("echo 'playing song" + songs[index] + "' | festival --tts")
            os.system(song)
            print("now playing song"+ songs[index])
            playing = True
        else:
            print("moved index to song "+ songs[index])

        sleep(1)  #pause in order to debounce buttons

    #if skip previous button is pressed
    if GPIO.input(skip_p)==0:

        print("Pressed skip to previous")

        #moved index to previous song, or to end of list
        if index > 0:
            index = index - 1
        else:
            index = len(songs)-1

        #if currently playing, stop playing and start next song
        if playing == True:
            os.system('pkill mpg123')
            playing = False

            song = 'mpg123 -q ' + songs[index] + '.mp3 &'
            os.system("echo 'playing song"+ songs[index] + "' | festival --tts")
            os.system(song)

            print("now playing song "+ songs[index])
            playing = True

        else:
            print("moved index to song "+ songs[index])

        sleep(1) #pause in order to debounce buttons

