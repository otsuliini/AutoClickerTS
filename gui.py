import PySimpleGUI as sg
import clicker

def create_window():
    layout = [
        [sg.Text("Auto Clicker")],
        [sg.Button("Start Clicking", key="start"), sg.Button("Stop Clicking", key="stop")],
        [sg.Button("Exit")]
    ]
    return sg.Window("Auto Clicker", layout)

def main():
    window = create_window()
    clicker_instance = clicker.Clicker()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "start":
            clicker_instance.start_clicking()
        elif event == "stop":
            clicker_instance.stop_clicking()

    window.close()

if __name__ == "__main__":
    main()
