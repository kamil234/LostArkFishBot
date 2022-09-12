from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

VK_CODE = {'a':0x41,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'q':0x51,
           'r':0x52,
           's':0x53,
           'w':0x57 }

x = 0

def reel():
    win32api.keybd_event(VK_CODE['e'], 0,0,0)
    time.sleep(.13)
    win32api.keybd_event(VK_CODE['e'],0 ,win32con.KEYEVENTF_KEYUP ,0)
    
def sleepy():
    sleep(6)
    print("Sleeping 5 seconds")

def cast():
    win32api.keybd_event(VK_CODE['e'], 0,0,0)
    time.sleep(.189)
    win32api.keybd_event(VK_CODE['e'],0 ,win32con.KEYEVENTF_KEYUP ,0)

def search():
    counter = 0
    fish_found = 0
    while keyboard.is_pressed('v') == False:
        while pyautogui.locateOnScreen('HUH.png',confidence=0.78) != None:
            reel()
            fish_found += 1
            print("Found " + str(fish_found) + " Fish")
            sleepy()
            cast()
            counter = 0
        else:
            if counter%10 == 0:
                print("Looking for fish...")
            sleep(.09)
            counter += 1
            if counter > 100:
                print("Did not find any fish for 10 seconds, resetting...")
                counter = 0
                cast()

print("Starting in 5..")
while x == 0: 
    sleep(5)
    cast()
    search()
            
