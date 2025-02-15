import pyautogui
import time
import threading
import config
class Clicker:
    def __init__(self):
        self.running = False
        self.thread = None

    def start_clicking(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click)
            self.thread.start()

    def stop_clicking(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def _click(self):
        while self.running:
            pyautogui.click()
            time.sleep(config.Config.clickinterval)  # Adjust the interval as needed