# Raspberry-PI-Surveillance-car-using-Bluetooth-Controller
Raspberry PI Surveillance car using VR Bluetooth Controller 
After looking into lot of projects on internet I came up with an idea of controlling Home appliances using Bluetooth Controller.


So basically this project has 2 main parts:


1)Hardware:Raspberry Pi 4 (or below), any cheap bluetooth controller i am using vr controller 
           few leds and jumper wires. 


2)Program: program is written in python.



before proceeding further we have to update the libraries of python so type the following commands

![image](https://user-images.githubusercontent.com/88006688/177688551-767700b1-cff1-4fb9-a8b6-2e955c0406c0.png)

After connecting the  bluetooth Controller to Raspberry Pi (connect by clicking on Bluetooth button on right corner of the screen) We have to identify the "event Number" that can be found by typing following comands on Termial 

![image](https://user-images.githubusercontent.com/88006688/177688594-aeea4768-4ecc-4dc6-b700-a4d466d1172b.png)

As it is showing me two events to identify which is my controller we have to write another comand i.e,
![image](https://user-images.githubusercontent.com/88006688/177688627-7aed2686-37c0-49ea-b0b4-de37aac906ce.png)

In the above image when i typed  "  cat /dev/input/event0   " (Then hit Enter obviously) on the terminal then pressed button on Controller nothing happend ,  after that i typed                           "  cat /dev/input/event1   " (Hit enter) then pressed button on the controller then some characters appeared on the screen.


NOTE:to Exit controller input mode press Ctrl+z

Here controller Event is found i,e "event1"


In this part first we have to Read the the values of bluetooth controller before we use it.

![image](https://user-images.githubusercontent.com/88006688/177688672-c87e4bd9-93a6-4c1d-8290-f24d6e1e500a.png)

the above program is helpful in finding the values of bluetooth controller when you run the program after updating all the libraries and press the button on the controller the respective Number will be printend on the screen as shown.

![image](https://user-images.githubusercontent.com/88006688/177688705-9d3dd484-bc29-4eee-8738-f12b85c6fd33.png)

as you can see when i pressed Key_w ---> respective number 17 is printed(in yellow)

Now find all the code numebrs for all the buttons of the controller.
![image](https://user-images.githubusercontent.com/88006688/177688741-a774b71f-442d-4974-ae0a-5c507cf67dd8.png)

After finding the numbers use then in a program to control any thing.....


Using the main.py file we can easyly controll motors using L298N motor Driver module.


