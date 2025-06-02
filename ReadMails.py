#!/usr/bin/python3
import pyautogui
import webbrowser
from time import sleep

EmailLink = "https://www.icloud.com/mail/"
webbrowser.open(EmailLink)
sleep(2)

Unread = None
while Unread is None:
    try:
        for i in range(1500):
            Unread = pyautogui.locateOnScreen('unread.png')
            sleep(1)
            pyautogui.click(Unread.left+5,Unread.top+5)
            pyautogui.scroll(-2)
            sleep(1)

    except:
        print("Can't find the picture")
        
    
