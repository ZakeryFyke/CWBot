import pyautogui
import pywinauto
import win32clipboard
import time
import random


# win32clipboard.OpenClipboard()
# data = win32clipboard.GetClipboardData()
# print(data)
#
# Get position of desired mouse click
#print(pyautogui.position())

# # #1424,396
# # pyautogui.click(1424, 396)
# #
# # pyautogui.typewrite("/go")
# # pyautogui.typewrite(["enter"])
# #
#
def get_textbox_position():
    return 1424, 396

def get_bottom_message_position():
    return 1422, 357

def get_copy_text_position():
    return 1466, 417

def get_quest_button_position():
    return 1787, 452

def get_quest_type_button_position():
    return 1240, 386

def hit_enter():
    pyautogui.typewrite(["enter"])

# def click_textbox():
#     pyautogui.click(textbox_position_x, textbox_position_y)



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

def copy_bottom_message():
    time.sleep(.5)
    right_click_bottom_message()
    time.sleep(.5)

    failure = click_button(copy)

    while (failure == -1):
        print("Failure")
        time.sleep(3)
        failure = click_button(copy)

    time.sleep(.25)

# Get the text of the most recent message in the chat window
def get_bottom_message_text():
    copy_bottom_message()

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

# Stops a foray by typing "/go" in the text box and pressing enter
def stop_foray():
    failure = click_button(textbox)
    while(failure == -1):
        time.sleep(5)
        failure = click_button(textbox)
    time.sleep(2)
    pyautogui.typewrite("/go")
    hit_enter()

def go_questing():
    rand = random.randint(1, 4)
    time.sleep(rand)
    failure = click_button(quest)

    while (failure == -1):
        time.sleep(5)
        failure = click_button(quest)

    rand = random.randint(2, 5)
    time.sleep(rand)
    click_button(quest_type)
    while (failure == -1):
        time.sleep(5)
        failure = click_button(quest_type)

def sleep_with_countdown(length):

    if(length < 1):
        return

    print("Sleeping for " + str(length) + " seconds.")

    for i in range(length, 1, -1):
        time.sleep(1)

        # Only print every 5 seconds
        if i%5 == 0:
            print(i)


def main():

    #deadmau5
    while(1<2):
        print("Getting text")
        text = get_bottom_message_text()
        if(r"/go" in text.lower()):
            print("FORAY DETECTED, ATTEMPTING TO STOP")
            stop_foray()
            print("Waiting roughly 3 minutes")
            # rand = random.randint(180, 220)
            # time.sleep(rand)
        elif("You'll be back" in text):
            time.sleep(10)

        elif("back in" in text):
            time.sleep(10)

        elif("stamina" in text.lower()):
            print("Attempting to go on quest")
            lines = str.splitlines(text)
            stamina_line = [line for line in lines if "Stamina" in line][0]

            if(len(stamina_line) > 0):

                stamina_line = stamina_line.split('/')

                if(len(stamina_line) > 0 and len(stamina_line[0]) > 0):
                    stamina = int(stamina_line[0][-1])
                    print("Stamina: " + str(stamina))

                    if(stamina > 0):
                        print("Questing.")
                        go_questing()
                        # Wait for the forest to be over
                        #time.sleep(480)
            else:
                print("Not enough Stamina.")

        rand = random.randint(600, 900)
        print("Interactivity sleep of: " + str(rand) + " seconds.")
        sleep_with_countdown(rand)

        click_button(me)



# textbox_position_x, textbox_position_y = get_textbox_position()
message_position_x, message_position_y = get_bottom_message_position()
# copy_text_position_x, copy_text_position_y = get_copy_text_position()
# quest_button_position_x, quest_button_position_y = get_quest_button_position()
# quest_type_button_position_x, quest_type_button_position_y = get_quest_type_button_position()

quest_type = "Forest.png"
me = "me.PNG"
quest = "quests.PNG"
textbox = "textbox.PNG"
copy = "copy.PNG"
#bottom = "bottom.PNG"

main()









#print(pyautogui.position())
# questsButton = pyautogui.locateOnScreen(r"C:\Users\Zakery\Downloads\quests.PNG")
# center_button = pyautogui.center(questsButton)
# pyautogui.click(center_button)
#
# time.sleep(5)
# forestsButton = pyautogui.locateOnScreen(r"C:\Users\Zakery\Downloads\forest.PNG")
# center_button = list(pyautogui.center(forestsButton))
# center_button[0] += random.randint(-50, 50)
# center_button[1] += random.randint(-10, 10)
# pyautogui.click(center_button[0], center_button[1])
#
