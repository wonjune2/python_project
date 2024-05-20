from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="비어있는 칸이 있습니다.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                  f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("userinfo.txt", "a") as file:
                save_input = f"{website_input.get()} | {email_username_input.get()} | {password_input.get()}\n"
                file.write(save_input)
            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "dnjswns@gmila.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generator_button = Button(width=15, text="Generator Password")
generator_button.grid(column=2, row=3)





add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()