import pyautogui
from time import sleep

# 选项: 59 962
# 幻境: 241 774
# 迷: 1135 476
# 自动: 1776 637
# wait 15s

def autoFantasy():
    # click options
    sleep(2)
    pyautogui.moveTo(59, 962, .5)
    print("cursor moved to options")
    pyautogui.click()
    # click fantasy
    sleep(1)
    pyautogui.moveTo(241, 774, .5)
    print("cursor moved to fantasy")
    pyautogui.click()
    # click random
    sleep(2)
    pyautogui.moveTo(1135, 476, .5)
    print("cursor moved to random")
    pyautogui.click()
    # click auto
    sleep(1)
    pyautogui.moveTo(1776, 637, .5)
    print("cursor moved to auto")
    pyautogui.click()
    # battle
    sleep(15)
    battle()


def battle():
    # click battle
    sleep(2)
    pyautogui.moveTo(1812, 901, .5)
    pyautogui.click()
    print("click battle")
    # click jump over
    sleep(12)
    pyautogui.move(0, 45, .5)
    pyautogui.click()
    print("click jump over")
    # click submit
    sleep(2)
    pyautogui.moveTo(1149, 781, .5)
    pyautogui.click()
    print("click submit")
    # click quit
    for i in range(0, 3):
        sleep(3)
        pyautogui.moveTo(1898, 571, .5)
        pyautogui.click()
        print("click quit")

if __name__ == '__main__':
    autoFantasy()