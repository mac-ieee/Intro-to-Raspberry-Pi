
import serial 

arduinoData = serial.Serial(‘/dev/ttyACM0’,9600)

i=0
while i<20:
    if arduinoData.inWaiting()>0:
        serialData=arduinoData.readline()
        print(str(serialData)[2:-5])
        print(serialData)
        i = i+1