import random
import time
import pyautogui


def autoMove():
    while 1:
        # 5秒钟移动一次鼠标(移动鼠标时间可以根据自己需要设定)
        time.sleep(5)
        x = 1500
        y = random.randint(100, 900)
        pyautogui.moveTo(x, y)
        print("cursor moved to: x=" + str(x) + ", y=" + str(y))
        pyautogui.click()


if __name__ == "__main__":
    autoMove()
