import evdev
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
# creates object 'gamepad' to store the data
# you can call it whatever you like
gamepad = InputDevice('/dev/input/event1')
# button code variables (change to suit your device)
aBtn = 22
bBtn = 35
cBtn = 21
dBtn = 36
up = 17
down = 45
left = 30
right = 32
print(gamepad)
# loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
       	 if event.value == 1:
            if event.code == cBtn:
                print("C")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
                 print("A")
            elif event.code == dBtn:
                print("D")
            elif event.code == up:
                print("up")
                GPIO.output(3,True)
                GPIO.output(5,False)
                GPIO.output(7,True)
                GPIO.output(8,False)
            elif event.code == down:
                print("down")
		GPIO.output(3,False)
                GPIO.output(5,True)
                GPIO.output(7,False)
                GPIO.output(8,True)
            elif event.code == left:
                print("left")
		GPIO.output(3,False)
		GPIO.output(5,True) 
                GPIO.output(7,True)
                GPIO.output(8,False) 
            elif event.code == right:
                print("right")
		GPIO.output(3,True)
                GPIO.output(5,False)
            	GPIO.output(7,False)
                GPIO.output(8,True)
	 if event.value == 0:
	    GPIO.output(3,False)
       	    GPIO.output(5,False)
            GPIO.output(7,False)
            GPIO.output(8,False)
