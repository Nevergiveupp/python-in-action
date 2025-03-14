import random
import time
import pyautogui


def autoMove():
    while 1:
        time.sleep(15)
        x = 10
        y = random.randint(1, 10)
        pyautogui.moveTo(x, y)
        print("cursor moved to: x=" + str(x) + ", y=" + str(y))
        pyautogui.click()


if __name__ == "__main__":
    autoMove()
