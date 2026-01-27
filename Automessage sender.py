import pyautogui
import time
message = 10

while message >=0:
    time.sleep(1)
    pyautogui.typewrite("I am a Hacker")
    time.sleep(1)
    pyautogui.press('Enter')
    message = message -1



