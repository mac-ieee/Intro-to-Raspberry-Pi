#############################
#   Adding two 3-bit 
#   binary numbers to 
#   produce a 4-bit number,
#   displayed on LEDs.
############################

import serial 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

chan_list = [40,22,29,31,32,33,35,36,37,38] 
GPIO.setup(chan_list,GPIO.OUT) 
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP) 

arduinoData = serial.Serial('/dev/ttyACM0',9600) 

carry = False 
num1 = [31,29,22] 
num2 = [35,33,32] 
sum = [36,37,38] 
in1 = [False,False,False] 
in2 = [False,False,False] 
sumout = [False,False,False] 
flag = True
al1 = 0 
val2 = 0 
total = 0 

while True: 
    if arduinoData.inWaiting() > 0: 
        serialData = arduinoData.readline() 
        in_value = int(str(serialData)[2:-5],10) 
        
        if flag==True: 

            if in_value >= 7*int(1023/8): 
                in1 = [True,True,True] 
                val1 = 7 
            elif in_value >= 6*int(1023/8): 
                in1 = [True,True,False] 
                val1 = 6 
            elif in_value >= 5*int(1023/8): 
                in1 = [True,False,True] 
                val1 = 5
            elif in_value >= 4*int(1023/8): 
                in1 = [True,False,False] 
                val1 = 4 
            elif in_value >= 3*int(1023/8): 
                in1 = [False,True,True] 
                val1 = 3 
            elif in_value >= 2*int(1023/8): 
                in1 = [False,True,False] 
                val1 = 2 
            elif in_value >= int(1023/8): 
                in1 = [False,False,True] 
                val1 = 1 
            else: 
                in1 =[False,False,False] 
                val1 = 0 
        
        else: 
            if in_value >= 7*int(1023/8): 
                in2 = [True,True,True] 
                val2 = 7 
            elif in_value >= 6*int(1023/8): 
                in2 = [True,True,False] 
                val2 = 6 
            elif in_value >= 5*int(1023/8): 
                in2 = [True,False,True] 
                val2 = 5 
            elif in_value >= 4*int(1023/8): 
                in2 = [True,False,False] 
                val2 = 4 
            elif in_value >= 3*int(1023/8): 
                in2 = [False,True,True] 
                val2 = 3 
            elif in_value >= 2*int(1023/8): 
                in2 = [False,True,False] 
                val2 = 2 
            elif in_value >= int(1023/8): 
                in2 = [False,False,True] 
                val2 = 1 
            else: 
                in2 =[False,False,False] 
                val2 = 0 
                
        if GPIO.input(18)==0: 
            if(flag == True): 
                flag = False 
            else: 
                flag = True 
        total = val1+val2 
            
        for i in range(3): 
            if total%2 == 1: 
                sumout[i] = True 
            else: 
                sumout[i] = False 
            
            total = int(total/2) 

        if(total == 1): 
            carry = True 
        else: 
            carry = False 
        
        GPIO.output(sum,sumout)
        GPIO.output(40,carry) 
        GPIO.output(num1,in1)
        GPIO.output(num2,in2)
