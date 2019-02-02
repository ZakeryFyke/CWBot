import pyautogui
import win32clipboard
import time
import random

def get_bottom_message_position():
    return 1408, 364

def get_bottom_message_text():
    copy_bottom_message()

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def copy_bottom_message():
    time.sleep(.5)
    right_click_bottom_message()
    time.sleep(.5)

    failure = click_button(copy)

    if(failure == -1):
        print("Failure")
        copy_bottom_message()

    # while (failure == -1):
    #     print("Failure")
    #     time.sleep(3)
     #     failure = click_button(copy)

    time.sleep(.25)

def click_button(button_path, type='left'):
    button = pyautogui.locateOnScreen(button_path)
    time.sleep(2)
    if (button != None):
        center_button = pyautogui.center(button)
        pyautogui.click(center_button, button=type)
        return None
    else:
        return -1

def right_click_bottom_message():
    pyautogui.click(message_position_x, message_position_y, button='right')

def hit_enter():
    pyautogui.typewrite(["enter"])

def stop_foray():
    print("Clicking in textbox.")
    # failure = click_button(textbox)
    # while(failure == -1):
    #     time.sleep(5)
    #     failure = click_button(textbox)
    print("sleeping")
    time.sleep(2)
    print("Typing /go")
    pyautogui.typewrite("/go")
    hit_enter()

    print("Waiting 5 minutes to defend")
    time.sleep(300)
    click_button(defend)

# Click off the window so the bot doesn't see all messages read instantly
def click_off_window():
    pyautogui.click(1355, 972)

message_position_x, message_position_y = get_bottom_message_position()

quest_type = "Forest.png"
me = "me.PNG"
quest = "quests.PNG"
textbox = "textbox.PNG"
copy = "copy.PNG"
defend = "defend.PNG"

while(True):

    print("Getting text")
    text = get_bottom_message_text()
    print(text)
    if(r"/go" in text.lower()):
        print("FORAY DETECTED, ATTEMPTING TO STOP")
        stop_foray()

    rand = random.randint(95, 120)
    print("Waiting " + str(rand) + " seconds")
    click_off_window()
    time.sleep(rand)

print(pyautogui.position())