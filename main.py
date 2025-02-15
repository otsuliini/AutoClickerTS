import clicker
import key_listener
import config
import threading
import time
import keyboard

def main():
    clicker_instance = clicker.Clicker()
    key_listener_instance = key_listener.KeyListener()
    keyboard.add_hotkey("f6", clicker_instance.start_clicking)
    keyboard.add_hotkey("f7", clicker_instance.stop_clicking)
    key_listener_instance.start_listener()

if __name__ == "__main__":
    main()

