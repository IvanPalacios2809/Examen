# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:01:22 2020

@author: LAST_
"""

import pyautogui
import time
i=False
x=False
c=0
screenWidth, screenHeight=pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.FAILSAFE=False

pyautogui.click(50,1080)

pyautogui.press('Windows')
pyautogui.write('https://es.pornhub.com/view_video.php?viewkey=ph5dc4b15d964e0')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('space')
time.sleep(1)
while(i!=True):
    pyautogui.press('volumeup')
   
    pyautogui.keyUp('alt')
    pyautogui.moveTo(960,540)
    pyautogui.write('f')
    