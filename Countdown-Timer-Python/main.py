import datetime
import os
import sys
import time
from tkinter import *
from tkinter import messagebox
import webbrowser

# ROOT - Main Single Window
root = Tk()
root.geometry("440x300")
root.resizable(False, False)
root.title("Countdown Timer")


# Merging into executable (Path)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# bg - Background image & my_github - GitHub logo
bg = PhotoImage(file=resource_path("bg.png"))
my_github = PhotoImage(file=resource_path("my_github.png"))

Label(root, image=bg).place(x=20, y=80)
root.iconphoto(False, bg)

# Hyperlinking logo
link_to_github = Label(root, image=my_github, cursor="hand2")
link_to_github.pack(side=LEFT, padx=4)
link_to_github.bind("<Button-1>", lambda e: callback("https://github.com/RealMosam"))

total_seconds = -1

# Textfield Boxes (type - String)
hour = StringVar()
minute = StringVar()
second = StringVar()

# Default entry values
hour.set("00")
minute.set("00")
second.set("00")

# Customizing textfields
Label(root, font=("Arial", 16, ""), text="Hours").place(x=85, y=10)
hourEntry = Entry(root, width=6, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=40)

Label(root, font=("Arial", 16, ""), text="Minutes").place(x=175, y=10)
minuteEntry = Entry(root, width=7, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=170, y=40)

Label(root, font=("Arial", 16, ""), text="Seconds").place(x=277, y=10)
secondEntry = Entry(root, width=7, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=272, y=40)


# Hyperlinking function
def callback(url):
    webbrowser.open_new_tab(url)


# Start button function
def start():
    global total_seconds
    try:
        # Converting entered data into integer type
        total_seconds = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        while total_seconds > -1:

            datetime.timedelta(seconds=total_seconds)

            mins, secs = divmod(total_seconds, 60)

            hours = 0

            if mins > 60:
                hours, mins = divmod(mins, 60)

            # Formatting entered data
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            # Updating main root window after every 1 second
            root.update()
            time.sleep(1)

            # Popup window when timer's time is over
            if total_seconds == 0:
                messagebox.showinfo("Countdown Timer", "Time's up!")
            total_seconds -= 1
    except:
        messagebox.showerror("Countdown Timer", "Enter only integer values.")


# Stop button function
def stop():
    global total_seconds
    total_seconds = -1


# Resume button function
def resume():
    start()


# Reset button function
def reset():
    global total_seconds
    hour.set("00")
    minute.set("00")
    second.set("00")
    total_seconds = -1


# Customizing buttons
btn = Button(root, text='Set Timer and Start', bd='5', activebackground='lightgreen',
             command=start)
btn.place(x=160, y=110)

btn2 = Button(root, text='Stop', bd='5', activebackground='red',
              command=stop)
btn2.place(x=188, y=150)

btn3 = Button(root, text='Resume', bd='5', activebackground='yellow',
              command=resume)
btn3.place(x=180, y=190)

btn4 = Button(root, text='Reset', bd='5', activebackground='lightblue',
              command=reset)
btn4.place(x=188, y=230)

# Infinite loop for running root window
root.mainloop()
