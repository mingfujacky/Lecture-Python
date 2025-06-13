# write a python program to make a mouse jiggling,  move it enough so I can see it. Stop when I move the mouse and print the current position of the mouse when it stops jiggling.
import pyautogui
import time
from pynput import mouse

stop_jiggle = False
last_pos = pyautogui.position()

def on_move(x, y):
    global stop_jiggle
    print(f"Mouse moved to ({x}, {y})")
    if (x, y) != last_pos:
        stop_jiggle = True
        return False  # Stop listener

# Start mouse listener in a separate thread
listener = mouse.Listener(on_move=on_move)
listener.start()

try:
    while not stop_jiggle:
        current_pos = pyautogui.position()
        # Move mouse slightly to the right and back
        pyautogui.move(100, 0, duration=1)
        time.sleep(0.1)
        pyautogui.move(-100, 0, duration=1)
        time.sleep(0.3)
except KeyboardInterrupt:
    pass

listener.stop()