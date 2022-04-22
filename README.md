# Battery_checker
Battery checker app made from tkinter and python to check your device battery and set notifications

This app is created by me to check your device's battery. It is a GUI app where you can set notifications on which battery percentage do you want to notify you. 
There are two settings where you can interact with. The first is the charged settings, this is used to set the battery percentage that you want your device 
to notify you on when you are charging your device. This is mostly used to notify you on which battery percentage do you want to stop charging at to ensure a healthy 
battery lifestyle. The second settings is the remains settings, this is used to set the battery percentage that you want your device to notify you when you are not 
charging your device. This is mostly used to notify you the battery percentage when you are not charging your device so that you can start to charged your device 
on that battery percentage that you have set. 
There are two python files. The first is the main.py file which is used to run the battery checker GUI. The second is the battery_GUI.py file. This file contains the code 
to set up the GUI and to be used n the main.py file. 

The GUI app also contains a top frame that shows your current battery percentage and your plugged in status.
The bottom frame of the GUI is used to set the notifications so that your device can notify you when your device has reach the battery percentage that you have set. 

This project imports tkinter, plyer, and psutil. We import the notifcations function from plyer and the sensor battery class from psutil. You will need to install both plyer and psutil by using pip in order to use this program.
