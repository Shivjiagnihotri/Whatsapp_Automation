import time
import pywhatkit
import pyautogui

x=["+9100000000","+9100000000"]
i=0
j=len(x)-1
k=0

#replaced ,+ with ","+
while i<=j:
    pywhatkit.sendwhatmsg_instantly(
        phone_no=x[i],
        message="This is a whatsapp message",
        chrome_path="C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2314.6.0_x64__cv1g1gvanyjgm"
        )
    time.sleep(25)
    pyautogui.press("enter")
    pyautogui.typewrite( "This is my additional msg")
    pyautogui.press("enter")
    time.sleep(2)
    i=i+1

