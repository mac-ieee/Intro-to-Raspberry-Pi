#############################
#   Test playing 
#   an mp3 file.
############################

import os 
from time import sleep 

song = ‘mpg123 -q name.mp3 &’ #replace ‘name.mp3’ with filename 

os.system(song) # play song 

print(“Now Playing: “, song[10:-2]) 
sleep(10) # play for 10 secs, then stop 

os.system(‘pkill mpg123’) # stop playing the file 

print(“Stopped playing.”)