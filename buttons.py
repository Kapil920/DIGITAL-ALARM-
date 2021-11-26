from tkinter import *
import time
import os

clk = Tk()
clk.title("Clock")
clk.geometry("1350x700+0+0")  # width, height, x-axis, y-axis
clk.config(bg="#0C1E28")


def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    print(hr, mn, sc)

    if int(hr) > 12 and int(mn) > 0:  # convert am to pm
        lb_dn.config(text="PM")
    if int(hr) > 12:
        hr = str(int(int(hr) - 12))

    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    lb_hr.after(200, clock)  # to update clock every second


# Hours
lb_hr = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#0975B7", fg="white")
lb_hr.place(x=350, y=200, width=150, height=150)

lb_hr_txt = Label(clk, text="HOUR", font=("Times 20 bold", 20, 'bold'), bg="#0975B7", fg="white")
lb_hr_txt.place(x=350, y=360, width=150, height=50)

# Minutes
lb_mn = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#008EA4", fg="white")
lb_mn.place(x=520, y=200, width=150, height=150)

lb_mn_txt = Label(clk, text="MINUTES", font=("Times 20 bold", 20, 'bold'), bg="#008EA4", fg="white")
lb_mn_txt.place(x=520, y=360, width=150, height=50)

# Seconds
lb_sc = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#06B4B8", fg="white")
lb_sc.place(x=690, y=200, width=150, height=150)

lb_sc_txt = Label(clk, text="SECOND", font=("Times 20 bold", 20, 'bold'), bg="#06B4B8", fg="white")
lb_sc_txt.place(x=690, y=360, width=150, height=50)

# AM-PM
lb_dn = Label(clk, text="AM", font=("Times 20 bold", 70, 'bold'), bg="#06B4B8", fg="white")
lb_dn.place(x=860, y=200, width=150, height=210)

#lb_dn_txt = Label(clk, text="AM/PM", font=("Times 20 bold", 20, 'bold'), bg="#06B4B8", fg="white")
#lb_dn_txt.place(x=860, y=360, width=150, height=50)


def b2():
    os.startfile("but1.py")


def b3():
    os.startfile("but2.py")


def b4():
    os.startfile("but3.py")


btn1 = Button(clk, text="Calendar", font=("Times 20 bold", 20), bg='black', fg='white', command=b2)
btn1.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.09)

btn2 = Button(clk, text="Alarm", font=("Times 20 bold", 20), bg='black', fg='white', command=b3)
btn2.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.09)

btn3 = Button(clk, text="To Do List", font=("Times 20 bold", 20), bg='black', fg='white', command=b4)
btn3.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.09)

clock()
clk.mainloop()
