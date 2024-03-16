import pyautogui, sys
import time

def autoDelete():
    i = 0
    while 1:
        time.sleep(5)

        pyautogui.moveTo(1572, 533)
        pyautogui.click()
        print("点击删除")

        time.sleep(2)

        pyautogui.moveTo(1266, 520)
        pyautogui.click()
        print("点击确认")

        i += 1
        print("已删除" + str(i) + "条记录")

if __name__ == "__main__":
    print('Start Delete...')
    autoDelete()