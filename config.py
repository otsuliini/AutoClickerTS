import time


class Config:
    def setConfig(self):
        print("Auto Clicker is running")
        print("Press F6 to start clicking")
        print("Press F7 to stop clicking")
        print("Press ESC to exit")
        print("Set The Click Interval")
        clickinterval = input("Enter the click interval (Default is 0.1 and max is 0.001): ")
        
    clickinterval = 0.1  # The interval between each click
    
    