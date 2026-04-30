import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open("Images/homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

start_button = tk.PhotoImage(file="Images/startbutton.png")
button = tk.Button(root, image=start_button, borderwidth=0, highlightthickness=0, relief="flat")

button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
