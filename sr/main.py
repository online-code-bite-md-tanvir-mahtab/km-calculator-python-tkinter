import tkinter


# creting the object of the tkinter
screen = tkinter.Tk()
screen.minsize(width=300,height=100)
screen.title("BMI Calculator")
screen.config(padx=10,pady=10)

text_input = tkinter.Entry()
text_input.grid(column=1,row=2)

# for the lable
my_label = tkinter.Label(text="Mils")
my_label.grid(column=2,row=2)


# for the sencond thing
equal = tkinter.Label(text="is equal to ")
equal.grid(column=0,row=3)

# for the answer
answer_screen = tkinter.Label(text="0")
answer_screen.grid(column=1,row=3)


# for the label
km = tkinter.Label(text="Km")
km.grid(column=2,row=3)


def calculation():
    result = int(1.6 * int(text_input.get()))
    answer_screen["text"] = result

# for the button
calculate= tkinter.Button(text="Calculate",command=calculation)
calculate.grid(column=1,row=4)








screen.mainloop()
