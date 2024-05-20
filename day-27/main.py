from tkinter import *


def button_clicked():
    st = input.get()
    my_label.config(text=st)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I Am a Label")
my_label["text"] = "new Text"
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()