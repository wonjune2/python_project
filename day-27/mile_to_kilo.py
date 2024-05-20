from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)

def mile_to_km_converter():
    mile_input = input.get()
    klio = round(int(mile_input) * 1.609)
    km.config(text=str(klio))
    pass

label = Label(text="is equal to")
label.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km = Label(text="0")
km.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=mile_to_km_converter)
button.grid(column=1, row=3)

window.mainloop()