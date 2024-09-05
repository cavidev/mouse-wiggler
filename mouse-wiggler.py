import pyautogui
import time
import random
import sys

pyautogui.FAILSAFE = False
screenSize = pyautogui.size()

def wiggle_mouse() -> None:
    """
    Wiggles the mouse between two coordinates.
    """
    x, y = pyautogui.position()
    
    pyautogui.moveTo(
        x= x + (-100), 
        y=y,
        duration=0.5
    )
    
    x, y = pyautogui.position()
    pyautogui.moveTo(
        x= x + (100), 
        y=y,
        duration=0.5
    )
    pyautogui.click()
    time.sleep(2)
    
if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        while True:
            wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")