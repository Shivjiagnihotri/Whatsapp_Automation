import time
import pywhatkit
import pyautogui

x=["+919860409418","+918208211933","+917972121958","+918208211933"]
i=0
j=len(x)-1
k=0


while i<=j:
    pywhatkit.sendwhatmsg_instantly(
        phone_no=x[i],
        message="*BIGGEST FELLOWSHIP PROGRAM* 🔥\n\n🕐One hour Aptitude Test🚀\n\n "
        "*This will be a great learning experience and help in preparing for entrances in your future.* \n"
        "*Additionally the test scores will be visible on recruiters dashboard to view while hiring so it will help you in getting a job.* \n\n"
        "✅ Rewards worth 2000 Rs to all Participants \n"
        "✅ Participation Certificate \n"

        "\n🔥 Enroll Now for Free 👇\n"
        "*https://bit.ly/3iIJRl2*\n"
        "*https://bit.ly/3iIJRl2*\n"

        "\nJoin Our Placement Group:- https://bit.ly/3WrUg2s\n"

        "\nAre you looking for Internship? Apply Now:-\n"
        "https://bit.ly/3GTLm88\n"

        "\n💫 Share it with your friends\n"

    )
    time.sleep(30)
    pyautogui.press("enter")
    time.sleep(5)
    # while k<=3:
    #     pyautogui.press("enter")
    #     k=k+1
    i=i+1

