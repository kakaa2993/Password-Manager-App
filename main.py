from tkinter import *

FONT = "Courier"


windows = Tk()
windows.title(string="My_Passwords")
windows.config(padx=20, pady=20)


canvas = Canvas(width=256, height=256)
my_photo = PhotoImage(file='my_password.png')
canvas.create_image(130, 130, image=my_photo,)
canvas.pack()






windows.mainloop()