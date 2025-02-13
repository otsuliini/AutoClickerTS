import clicker
import key_listener
import gui
import config
import threading
import time
import keyboard


def main():
    
    keyboard.add_hotkey("f6", clicker.Clicker().start_clicking)
    keyboard.add_hotkey("f7", clicker.Clicker().stop_clicking)

if __name__ == "__main__":
    main()

