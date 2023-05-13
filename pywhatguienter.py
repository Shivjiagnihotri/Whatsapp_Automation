import time 
import pywhatkit
import pyautogui



nums=["+919890739418","+918208211933"]



	pywhatkit.sendwhatmsg_instantly(
            phone_no=x, 
            message="msg"
            
        )

time.sleep(25)
count=0
while count<=50:
    
    pyautogui.press("enter")
    count=count+1