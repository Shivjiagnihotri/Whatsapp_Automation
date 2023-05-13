import pyautogui
import time
time.sleep(4)
count=0
while count<=50:
    pyautogui.typewrite("tc")
    pyautogui.press("enter")
    count=count+1