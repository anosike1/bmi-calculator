from tkinter import *

window = Tk()
window.title ("BMI Calculator")

lab1 = Label (text="Weight (in kilograms)")
lab1.grid (column=0, row=1)

lab2 = Label (text="Height (in metres)")
lab2.grid (column=0, row=2)

lab3 = Label (text="")
lab3.grid (column=1, row=4)

entry1 = Entry ()
entry1.grid (column=1, row=1)

entry2 = Entry ()
entry2.grid (column=1, row=2)

def bmi():
    wt = float (entry1.get())
    ht = float (entry2.get())
    bmii = round (wt/(ht**2),2)
    lab3.config (text=f"Your BMI is {bmii}kg/m2")

btn = Button (text="Calculate", command=bmi)
btn.grid (column=1, row=3)


mainloop()