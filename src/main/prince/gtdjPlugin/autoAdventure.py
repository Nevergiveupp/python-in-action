import pyautogui
from time import sleep

# 启程: 1824 974
# 奇遇(2): 1843 238
# 前往: 1154 881
# 出战: 1812 901
# 自动: 1848 418
# 跳过战斗: 1816 946
# 确定: 1149 781
# 退出(2): 1898 571


def autoAdventure():
    # click start
    x=1824
    y=980
    pyautogui.moveTo(x, y, .5) # 这里不加duration会导致鼠标移动不到最右边
    print("cursor moved to: x=" + str(x) + ", y=" + str(y))
    print(pyautogui.position())
    print(pyautogui.onScreen(1824, 980))
    pyautogui.click()
    # click adventure
    sleep(8)
    for i in range(0, 2):
        pyautogui.moveTo(1843, 238, .5)
        pyautogui.click()
        sleep(2)
    # click go to
    sleep(6)
    pyautogui.moveTo(1154, 881, .5)
    pyautogui.click()
    # click battle
    sleep(8)
    pyautogui.moveTo(1812, 901, .5)
    pyautogui.click()
    # click auto
    sleep(10)
    pyautogui.moveTo(1848, 418, .5)
    pyautogui.click()
    # click jump over
    sleep(1)
    pyautogui.moveTo(1816, 946, .5)
    pyautogui.click()
    # click submit
    sleep(2)
    pyautogui.moveTo(1149, 781, .5)
    pyautogui.click()
    # click quit
    for i in range(0, 3):
        sleep(5)
        pyautogui.moveTo(1898, 571, .5)
        pyautogui.click()

if __name__ == '__main__':
    autoAdventure()