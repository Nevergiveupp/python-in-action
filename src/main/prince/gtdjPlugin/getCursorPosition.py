import pyautogui
from time import sleep


if __name__ == "__main__":
    try:
        while True:
            sleep(2)
            x, y = pyautogui.position()
            print(x, y)
    except KeyboardInterrupt:
        print('\nExit.')
