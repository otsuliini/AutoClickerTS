import pyautogui
import keyboard
import time
import threading

class KeyListener:
    def on_Shortcut(self):
        print("Auto Clicker is running")

    def start_listener(self):
        keyboard.add_hotkey("ctrl+shift+a", self.on_Shortcut)
        keyboard.wait("esc")