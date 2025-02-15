import clicker
import key_listener
import gui
import config
import threading
import time
import keyboard


def main():
    clicker_instance = clicker.Clicker()
    keyboard.add_hotkey("f6", clicker_instance.start_clicking)
    keyboard.add_hotkey("f7", clicker_instance.stop_clicking)
    
if __name__ == "__main__":
    main()

