# Import modules
from tkinter import *
from plyer import notification
from psutil import sensors_battery

width = 720
height = 360
notify = False
notify_remains = 0
notify_charging = 0
notified_charged = False
notified_remains = False

# function to measure the width or height of the gui to be used for size or placement of frames or buttons
def prct(prct, length):
    return (prct * length) // 100

# used the up buttons to increase the percentages of remains and charged for the notifications settings
def upsetting(label, remain, button):
    if label["text"] == "--":
        label["text"] = "01"
        button["state"] = "normal"
    elif label["text"] != "--":
        if (remain is True and label["text"] == "99") or (remain is False and label["text"] == "100"):
            return None
        else:
            current = int(label["text"]) + 1
            fixed_current = "0" + str(current) if current < 10 else str(current)
            label["text"] = fixed_current

# used to decrease the percentage of remains and charged for the notifications settings
def downsetting(label, other_label, button):
    if label["text"] == "01":
        label["text"] = "--"
    elif label["text"] != "--":
        current = int(label["text"]) - 1
        fixed_current = "0" + str(current) if current < 10 else str(current)
        label["text"] = fixed_current
    if label["text"] == "--" and other_label["text"] == "--":
        button["state"] = "disabled"

class battery_settings:
    battery_text = None
    plugged_text = None
    remainset = None
    charging_set = None
    Set_button = None
    upremain_button = None
    downremain_button = None
    upcharged_button = None
    downcharged_button = None

    # the text to set the percentage notification
    @staticmethod
    def create_bottomtext(location):
        battery_settings.remainset = Label(location, text="--", bg="black", fg="white", font=("Verdana bold", 20))
        battery_settings.remainset.place(x=prct(17, width), y=65)
        battery_settings.charging_set = Label(location, text="--", bg="black", fg="white", font=("Verdana bold", 20))
        battery_settings.charging_set.place(x=prct(74, width), y=65)

    # method to create the battery percentage and plugged status label
    @staticmethod
    def create_uppertext(location):
        battery_settings.battery_text = Label(
            location,
            text="00",
            bg="#4A7A8C",
            font=("Verdana bold", 35))
        battery_settings.plugged_text = Label(
            location,
            text="Not charging",
            bg="#4A7A8C",
            font=("Verdana bold", 15)
        )

    # static method to create the buttons
    @staticmethod
    def create_button(location):
        upremain = Button(
            location,
            width=5, text="^",
            command=lambda: upsetting(battery_settings.remainset, remain=True, button=battery_settings.Set_button))
        upremain.place(x=prct(30, width), y=65)
        downremain = Button(
            location,
            width=5, text="▼",
            command=lambda: downsetting(battery_settings.remainset, battery_settings.charging_set, battery_settings.Set_button))
        downremain.place(x=prct(30, width), y=prct(25, height))
        upcharge = Button(
            location, width=5, text="^",
                          command=lambda: upsetting(battery_settings.charging_set, remain=False, button=battery_settings.Set_button))
        upcharge.place(x=prct(85, width), y=65)
        downcharge = Button(location, width=5, text="▼",
                            command=lambda: downsetting(battery_settings.charging_set, battery_settings.remainset, battery_settings.Set_button))
        downcharge.place(x=prct(85, width), y=prct(25, height))
        battery_settings.upremain_button = upremain
        battery_settings.downremain_button = downremain
        battery_settings.upcharged_button = upcharge
        battery_settings.downcharged_button = downcharge
        Set_button = Button(location, width=10, text="Set",
                            command=lambda: set_notifications(location, Set_button))
        Set_button["state"] = "disabled"
        Set_button.place(
            x=prct(46, width), y=prct(34, height))
        battery_settings.Set_button = Set_button


# function to constantly check the battery and make notifications if set
def constant_check():
    global notified_charged
    global notified_remains
    battery_checker = sensors_battery()
    battery_settings.battery_text["text"] = battery_checker.percent
    battery_settings.plugged_text["text"] = "Charging" if battery_checker.power_plugged else "Not charging"
    if notify:
        if battery_checker.power_plugged:
            notified_remains = False
            if battery_checker.percent == notify_charging and notified_charged is not True:
                notification.notify(
                    # title of notification
                    title="Plugged In",

                    # message of notification
                    message=f"Your device has been charged up to {notify_charging}, please unplug your charger if you do not wish to continue charging.",

                    # displaying time
                    timeout=5
                )
                notified_charged = True
        else:
            notified_charged = False
            if battery_checker.percent == notify_remains and notified_remains is not True:
                notification.notify(
                    # title of notification
                    title="Battery remainings",

                    # message of notification
                    message=f"Your device's battery is now at {notify_remains}% remaining. Please charge your device now.",

                    # displaying time
                    timeout=5
                )
                notified_remains = True
    battery_settings.battery_text.after(1000, constant_check)

# function to be used for set button to set the notifications
def set_notifications(location, button):
    global notify
    notify = True
    global notify_charging
    global notify_remains
    global notified_charged
    global notified_remains
    notified_charged = False
    notified_remains = False
    button = Button(location, width=10, text="Change", command=lambda: off_notifications(location, button))
    button.place(x=prct(46, width), y=prct(34, height))
    battery_settings.Set_button = button
    battery_settings.upremain_button["state"] = "disabled"
    battery_settings.downremain_button["state"] = "disabled"
    battery_settings.upcharged_button["state"] = "disabled"
    battery_settings.downcharged_button["state"] = "disabled"
    if battery_settings.remainset["text"] != "--":
        notify_remains = int(battery_settings.remainset["text"])
    if battery_settings.charging_set["text"] != "--":
        notify_charging = int(battery_settings.charging_set["text"])


# used as command for the set button to turn off the notification so that user can change the settings of the notifications
def off_notifications(location, button):
    global notify
    notify = False
    button = Button(location, width=10, text="Set", command=lambda: set_notifications(location, button))
    button.place(x=prct(46, width), y=prct(34, height))
    battery_settings.Set_button = button
    battery_settings.upremain_button["state"] = "normal"
    battery_settings.downremain_button["state"] = "normal"
    battery_settings.upcharged_button["state"] = "normal"
    battery_settings.downcharged_button["state"] = "normal"



