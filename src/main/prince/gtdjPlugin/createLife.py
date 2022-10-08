import pyautogui
from time import sleep

# 选项: 59 962
# 异闻: 246 351
# 灵脉: 452 524
# 创命: 851 524
# 创命扫荡: 1312 929
# 创命扫荡结算取消: 1713 481
# 剑论: 1571 563
# 剑论扫荡: 1312 929

def scanCreateLife():
    # click options
    sleep(2)
    moveToPosition(59, 962)
    print("cursor moved to options")
    pyautogui.click()
    # click strange news
    sleep(1)
    moveToPosition(246, 351)
    print("cursor moved to strange news")
    pyautogui.click()
    # click create life
    sleep(1)
    moveToPosition(851, 524)
    print("cursor moved to create life")
    pyautogui.click()
    # scan once
    sleep(1)
    moveToPosition(1312, 929)
    print("cursor moved to scan button")
    pyautogui.click()
    # scan cancel
    sleep(1)
    moveToPosition(1713, 481)
    print("cursor moved to scan button")
    pyautogui.click()



def moveToPosition(x, y):
    pyautogui.moveTo(x, y)


if __name__ == '__main__':
    scanCreateLife()