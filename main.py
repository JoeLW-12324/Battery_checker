# importing modules
from tkinter import *
from threading import Thread
import battery_GUI
from battery_GUI import battery_settings

def main():
    # main function to execute the gui
    root = Tk()
    root.title("Battery checker")
    root.resizable(0, 0)
    root.geometry(f"{battery_GUI.width}x{battery_GUI.height}")
    root.configure(bg="#4A7A8C")
    root.iconbitmap("battery.ico")
    # frames settings
    top_frame = Frame(
        root,
        bg="#4A7A8C",
        width=battery_GUI.width,
        height=battery_GUI.prct(50,battery_GUI.height)
    )
    top_frame.place(x=0, y=0)
    bottom_frame = Frame(
        root,
        bg="black",
        width=battery_GUI.width,
        height=battery_GUI.prct(50,battery_GUI.height)
    )
    bottom_frame.place(x=0, y=battery_GUI.prct(50,battery_GUI.height))

    # creating buttons
    battery_settings.create_button(bottom_frame)

    # all of the label
    battery_label = Label(top_frame, text="Battery", font=("Verdana bold", 20), bg="#4A7A8C").place(
        x=battery_GUI.prct(40, battery_GUI.width), y=battery_GUI.prct(3, battery_GUI.height))

    percentage_text = Label(top_frame, text="%", bg="#4A7A8C", font=("Verdana bold", 15)).place(
        x=battery_GUI.prct(55, battery_GUI.width), y=battery_GUI.prct(25, battery_GUI.height))

    # bottom frame label
    settings = Label(bottom_frame, text="Notification", font=("Verdana bold", 20), bg="black", fg="white").place(
        x=battery_GUI.prct(38, battery_GUI.width), y=battery_GUI.prct(3, battery_GUI.height)
    )
    battery_remaining = Label(bottom_frame, text="Remain", bg="black", fg="white", font=("bold")).place(
        x=battery_GUI.prct(15, battery_GUI.width), y=battery_GUI.prct(10, battery_GUI.height)
    )
    battery_charged = Label(bottom_frame, text="Charge limit", bg="black", fg="white", font=("bold")).place(
        x=battery_GUI.prct(70, battery_GUI.width), y=battery_GUI.prct(10, battery_GUI.height)
    )

    # the text to show the percentage of the computer and is plugged or not
    battery_settings.create_uppertext(top_frame)
    battery_settings.create_bottomtext(bottom_frame)
    battery_settings.battery_text.place(
        x=battery_GUI.prct(43, battery_GUI.width), y=battery_GUI.prct(20, battery_GUI.height)
    )
    battery_settings.plugged_text.place(
        x=battery_GUI.prct(65, battery_GUI.width),y=battery_GUI.prct(25, battery_GUI.height)
    )

    # method from battery_GUI to constantly check the battery
    checking_thread = Thread(target=battery_GUI.constant_check())
    checking_thread.start()

    root.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

