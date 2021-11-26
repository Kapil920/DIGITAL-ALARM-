import os
from tkinter import *
import time
import datetime
from pygame import mixer
import random

root = Tk()
root.title('Alarm-Clock')


# root.geometry("500x400+0+0")  # width, height, x-axis, y-axis
# root.config(bg="#0C1E28")


def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if (alarmtime != "::"):
        alarmclock(alarmtime)


def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(root, font=('arial', 20, 'bold'),
                           text="Wake up!Wake up!Wake up", bg="DodgerBlue2", fg="white").grid(row=6, columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load('Alarm Tone.mp3')
            mixer.music.play(-1)
            while True:

                print("Press 'p' to pause")
                print("Press 'e' to exit the program")
                query = input("  ")

                if query == 'p':
                    # Pausing the music
                    zzz = random.randint(0, 1)
                    if zzz == 0:
                        os.startfile('game1.pyw')
                    elif zzz == 1:
                        os.startfile('game2.pyw')
                    mixer.music.stop()

                elif query == 'e':

                    # Stop the mixer
                    mixer.music.stop()
                    break
            break


hrs = StringVar()
mins = StringVar()
secs = StringVar()
greet = Label(root, font=('arial', 20, 'bold'),
              text="Take a short nap!").grid(row=1, columnspan=3)
hrbtn = Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'bold'))
hrbtn.grid(row=2, column=1)
minbtn = Entry(root, textvariable=mins,
               width=5, font=('arial', 20, 'bold')).grid(row=2, column=2)
secbtn = Entry(root, textvariable=secs,
               width=5, font=('arial', 20, 'bold')).grid(row=2, column=3)
setbtn = Button(root, text="set alarm", command=setalarm, bg="DodgerBlue2",
                fg="white", font=('arial', 20, 'bold')).grid(row=4, columnspan=3)
timeleft = Label(root, font=('arial', 20, 'bold'))
timeleft.grid()

root.mainloop()
