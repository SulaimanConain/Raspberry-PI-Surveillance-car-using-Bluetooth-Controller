#import evdev

from evdev import InputDevice, categorize, ecodes

#creates object gamepad to store the data
#you can call whatever you like

gamepad = InputDevice('/dev/input/event3')

#prints out devI
print (gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
  print(categorize(event))
