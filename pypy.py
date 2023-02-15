import time
import pywhatkit
import pyautogui

x=["+91-XXXXXXXXXX","+91-XXXXXXXXXX"]
i=0
j=len(x)-1
k=0


while i<=j:
    pywhatkit.sendwhatmsg_instantly(
        phone_no=x[i],
        message="*HEY HELLO! I INVITE YOU TO THIS GREAT LEARNING PROGRAM* 🔥\n\n🕐 One hour Aptitude Test 🚀\n\n"
        "*This will be a great learning experience and help in preparing for entrances in your future.* \n\n"
        "*Date:- 12th February 2023* \n"
        "*Time:-* 11:00 AM- 7:00 PM \n"
        "*Duration:- 60 Mins* \n\n"
        "✅ Rewards worth 2000 Rs to all Participants  \n"
        "✅ Participation *Certificate* 🤩 \n"

        "\n🔥 Enroll Now for Free 👇\n"
        "*https://bit.ly/3iIJRl2*\n"
        "*https://bit.ly/3iIJRl2*\n"

        "\n💫 Join Our Community for Updates:- https://bit.ly/3WrUg2s\n"

        "\nAre you looking for an Internship? Register to apply:-\n"
        "https://bit.ly/3GTLm88\n"

        "\n Note:- Reply with OK to activate the links.\n"

    )
    time.sleep(30)
    pyautogui.press("enter")
    time.sleep(5)
    # while k<=3:
    #     pyautogui.press("enter")
    #     k=k+1
    i=i+1

