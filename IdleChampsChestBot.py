from pyautogui import *
import pyautogui
import time
import keyboard
import random

#silverchest
#RGB: (124,  83,  52)
#X: 1975   Y:124

#goldchest
#RGB: (124,  83,  52)
#X: 1983?   Y:124?

#openmultiplechest
#X: 2055 Y:  140

#chestslider - red
#X: 2665 Y:  420
#RGB: ( 71,  28,   5)

#chestslider - yellow
#X: 2648 Y:  420
#RGB: (225, 110,   0)

#flipallcardsbutton - l
#X: 2647 Y:  387
#RGB: (254, 254, 254)

#See All Loot
#X: 2663 Y:  388
#(254, 254, 255)

#Close The Loot Window
#(x=3051, y=106)
#RGB: (173,   0,   0)

#Single chest done button
#
#

#     pyautogui.displayMousePosition()

print('Press Ctrl-C to quit.')
    
def start():
    try:
        while keyboard.is_pressed('Esc') == False:
            if pyautogui.pixelMatchesColor(2648, 419, (225, 110,   0)):
                #click open
                pyautogui.click(x=2478, y=463)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(3051, 106, (173,   0,   0)):
                #click close loot window
                pyautogui.click(x=3051, y=106)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(2663, 388, (254, 255, 255), tolerance=2):
                #click see all loot
                pyautogui.click(x=2663, y=388)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(2647, 387, (254, 254, 254)):
                #click flip all cards
                pyautogui.click(x=2647, y=387)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(2665, 420, ( 71,  28,   5)):
                #click the slider
                pyautogui.click(x=2665, y=420)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(2633, 383, (254, 254, 255), tolerance=2):
                #click single chest done button
                pyautogui.click(x=2633, y=383)
                time.sleep(0.1)
                continue
            if pyautogui.pixelMatchesColor(1975, 124, (124,  83,  52)):
                #click the chest
                pyautogui.click(x=2055, y=140)
                time.sleep(0.1)
    except KeyboardInterrupt:
        print('\n')

try:
    while True:
        time.sleep(0.5)
        if keyboard.is_pressed('ctrl+shift+plus'):
            start()
            
except KeyboardInterrupt:
    print('\n')
