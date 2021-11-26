# importing tkinter
from tkinter import *
# importing calendar module
import calendar


# initializing tkinter
clk = Tk()
# setting title of our Gui
clk.title("Gui Calendar")
# year for which we want the calendar to be shown on our Gui
clk.minsize(width=400, height=400)
clk.geometry("600x500")
year = 2021
# storing 2020 year calendar data inside myCal

myCal = calendar.calendar(year)
# showing calendar data using label widget
cal_year = Label(clk, text=myCal, font="Consolas 10 bold")
# packing the Label widget
cal_year.pack()
# running the program in ready state




clk.mainloop()