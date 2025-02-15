import time

class Config:
    clickinterval = 0.1  # The interval between each click

    @staticmethod
    def setConfig():
        print("Auto Clicker is running")
        print("Press F6 to start clicking")
        print("Press F7 to stop clicking")
        print("Press ESC to exit")
        print("Set The Click Interval")
        try:
            interval = float(input("Enter the click interval (Default is 0.1 and max is 0.001 but 0.001 doesn't really work that well :) OOH also the like longest interval is 1000 secs): "))
            if 0.001 <= interval <= 1000:
                Config.clickinterval = interval
            else:
                print("Invalid interval. Using default value of 0.1.")
        except ValueError:
            print("Invalid input. Using default value of 0.1.")
        print(f"Click interval set to {Config.clickinterval} seconds.")

