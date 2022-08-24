from tkinter import *

FONT = "Courier"


# Save the data into a data.txt file
def save_data():
    website = website_entry.get()
    email_or_username = Email_or_username_entry.get()
    password = password_entry.get()
    if website != "" and email_or_username != "" and password != "":
        with open("data.txt", "a+") as file:
            file.write(f"{website} | {email_or_username} | {password}\n")
            website_entry.delete(0, END)
            Email_or_username_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        print("there is something missing!")



windows = Tk()
windows.title(string="My Passwords")
windows.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
my_photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_photo,)
canvas.grid(column=1, row=0)

# Create Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

Email_or_username_label = Label(text="Email/Username:")
Email_or_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create Entries
website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

Email_or_username_entry = Entry(width=51)
Email_or_username_entry.grid(column=1, row=2, columnspan=2)
Email_or_username_entry.insert(0, "example@example.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Create Buttons

Add_button = Button(width=43, text="Add", command=save_data)
Add_button.grid(column=1, row=4, columnspan=2)

Generate_password_button = Button(text="Generate Password")
Generate_password_button.grid(column=2, row=3)







windows.mainloop()