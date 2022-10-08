import pyautogui
from time import sleep


if __name__ == "__main__":
    try:
        while True:
            sleep(0.5)
            x, y = pyautogui.position()
            print(x, y)
    except KeyboardInterrupt:
        print('\nExit.')
