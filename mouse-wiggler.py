import pyautogui
import time
import random
import sys

pyautogui.FAILSAFE = False
screenSize = pyautogui.size()
negative = -1

def wiggle_mouse() -> None:
    """
    Wiggles the mouse between two coordinates.
    """
    global negative
    x, y = pyautogui.position()
    
    pyautogui.moveTo(
        x= x + negative*10, 
        y=y,
        duration=1
    )
    negative = 1 if negative == -1 else -1
    time.sleep(10)
    
if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        
        while True:
            wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")