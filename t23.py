#!/usr/bin/python3
import pyautogui
from time import sleep

pyautogui.press('win')
sleep(1)
pyautogui.write('vs')

vsicon = None
while(vsicon==None):
    try:
       vsicon = pyautogui.locateOnScreen('vs.png')
       sleep(1)
       pyautogui.click(vsicon.left,vsicon.top)
    except pyautogui.ImageNotFoundException:
        print("can't find image try again")

exticon = None
while(exticon==None):
    try:
        exticon = pyautogui.locateOnScreen('exten.png')
        sleep(1)
        pyautogui.click(exticon.left,exticon.top)
        sleep(1)
    except pyautogui.ImageNotFoundException:
        print("can't find image try again")

pyautogui.write('cmake')
sleep(1)
Cmakext = None
inst1 = None
while(Cmakext==None and inst1==None):
    try:
        Cmaketxt = pyautogui.locateOnScreen('cmake.png')
        sleep(1)
        inst1 = pyautogui.locateOnScreen('ins.png')
        pyautogui.click(inst1.left+10,inst1.top+5)
        sleep(1)

        Ctoolext = None
        inst2 = None
        while(Ctoolext==None and inst2==None):
            try:
                Ctoolext = pyautogui.locateOnScreen('ctool.png')
                sleep(1)
                inst2 = pyautogui.locateOnScreen('ins2.png')
                pyautogui.click(inst2.left+10,inst2.top+5)

            except pyautogui.ImageNotFoundException:
                print("can't find image try again")  
    except pyautogui.ImageNotFoundException:
        print("can't find image try again")



