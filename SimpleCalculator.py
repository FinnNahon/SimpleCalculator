#Import Everything
from tkinter import *

#Initialize Tkinter
if __name__ == "__main__":
    CALCGUI = Tk()

#Configure Colour, Title & Size of Calculator
CALCGUI.configure(background="white")
CALCGUI.title("Finn's Amazing Calculator")
#CALCGUI.geometry("370x380")

#Entry Field
e = Entry(CALCGUI, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Button Add Command For Clicking Buttons
def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#Clear Button Function
def button_clear():
    e.delete(0, END)

#Add Button Function
def button_add():
    firstnumber = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstnumber)
    e.delete(0, END)

#Equal Button Function
def button_equal():
    secondnumber = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(secondnumber))
    if math == "subtract":
        e.insert(0, f_num - int(secondnumber))
    if math == "multiply":
        e.insert(0, f_num * int(secondnumber))
    if math == "division":
        e.insert(0, f_num / int(secondnumber))


#Subtract Button Function
def button_subtract():
    firstnumber = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(firstnumber)
    e.delete(0, END)

#Multiply Button Function
def button_multiply():
    firstnumber = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(firstnumber)
    e.delete(0, END)

#Divide Button Function
def button_divide():
    firstnumber = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(firstnumber)
    e.delete(0, END)

#Initialize Buttons 0-9
button_1 = Button(CALCGUI, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(CALCGUI, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(CALCGUI, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(CALCGUI, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(CALCGUI, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(CALCGUI, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(CALCGUI, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(CALCGUI, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(CALCGUI, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(CALCGUI, text="0", padx=40, pady=20, command=lambda: button_click(0))

#Initialize Functional Buttons
button_addition = Button(CALCGUI, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(CALCGUI, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(CALCGUI, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(CALCGUI, text="/", padx=41, pady=20, command=button_divide)
button_equals = Button(CALCGUI, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(CALCGUI, text="Clear", padx=78, pady=20, command=button_clear)

#Put Buttons On The Screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_addition.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

#End Of Code
CALCGUI.mainloop()