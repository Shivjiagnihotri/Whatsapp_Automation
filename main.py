import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()
i=1
x=["+9100000000","+9100000000"]
j=len(x)-1

def send_whatsapp_message(msg: str):
    try:
	  while i<=j:
        	pywhatkit.sendwhatmsg_instantly(
            	phone_no=x[i], 
            	message=msg,
            	tab_close=False
        	)
        	i=i+1
        	time.sleep(40)
        
	count=0
	while count<=500:
    		pyautogui.press("enter")
    		count=count+1
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="Test message from a Python script!")
