import pyautogui
import threading
import time
import config
class Clicker:
    def __init__(self):
        self.clicking = False
        self.thread = None

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.thread = threading.Thread(target=self._click)
            self.thread.start()

    def stop_clicking(self):
        if self.clicking:
            self.clicking = False
            self.thread.join()

    def _click(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(config.Config.clickinterval)  # Adjust the interval as needed