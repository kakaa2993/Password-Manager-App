from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = "Courier"
labels_background = "#002B5B"
entry_background = "#1CD6CE"
foreground = "#F6F6F6"

# Generate a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # Clear the password entry
    password_entry.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(index=0, string=password)
    # Copy the password to the clipboard
    pyperclip.copy(password)


# Save the data into a data.txt file
def save_data():
    website = website_entry.get()
    email_or_username = Email_or_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_or_username,
            "password": password,
        }
    }
    if len(website) == 0 or len(email_or_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the detail entered: \nEmail/Username: {email_or_username}"
                                               f"\nPassword: {password}\n\nDo you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(fp=data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                # Create the file
                with open("data.json", "w") as data_file:
                    json.dump(obj=new_data, fp=data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # Saving updating data
                    json.dump(obj=data, fp=data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Read the data
            data = json.load(fp=data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=website,
                                message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No detail for the website exists")



windows = Tk()
windows.title(string="My Passwords")
windows.config(padx=50, pady=50, background=labels_background)

canvas = Canvas(width=200, height=203, bg=labels_background, highlightthickness=0)
my_photo = PhotoImage(file='logo.png')
canvas.create_image(100, 103, image=my_photo, )
canvas.grid(column=1, row=0)

# Create Labels
website_label = Label(text="Website:", fg=foreground, bg=labels_background, padx=15, pady=5)
website_label.grid(column=0, row=1)

Email_or_username_label = Label(text="Email/Username:", fg=foreground, bg=labels_background, padx=15, pady=5)
Email_or_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", fg=foreground, bg=labels_background, padx=15, pady=5)
password_label.grid(column=0, row=3)

# Create Entries
website_entry = Entry(width=32, fg=foreground, bg=labels_background)
website_entry.grid(column=1, row=1)
website_entry.focus()

Email_or_username_entry = Entry(width=51, fg=foreground, bg=labels_background)
Email_or_username_entry.grid(column=1, row=2, columnspan=2)
Email_or_username_entry.insert(0, "example@example.com")

password_entry = Entry(width=32, fg=foreground, bg=labels_background)
password_entry.grid(column=1, row=3)

# Create Buttons

Add_button = Button(width=43, text="Add", command=save_data, fg="#8FE3CF", bg="#002B5B")
Add_button.grid(column=1, row=4, columnspan=2)

Generate_password_button = Button(text="Generate Password", command=generate_password, fg="#8FE3CF", bg="#2B4865")
Generate_password_button.grid(column=2, row=3)

Search_button = Button(text="Search", command=find_password, fg="#8FE3CF", bg="#2B4865", width=15)
Search_button.grid(column=2, row=1)
windows.mainloop()
