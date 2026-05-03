import tkinter as tk
from PIL import Image, ImageTk



root = tk.Tk()
image = Image.open("Images/homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

start_button = tk.PhotoImage(file="Images/startbutton.png")
button = tk.Button(root, image=start_button, relief="flat", cursor="hand2")
button.place(relx=0.5, rely=0.6, anchor="center")

def on_enter(event):
    button.config(bg="#2b58a6")

def on_leave(event):
    button.config(bg="#182156")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

username_entry = tk.Entry(root, font=("Arial", 14), bd=2, width=20)
username_entry.place(relx=0.5, rely=0.5, anchor="center")
username_entry.insert(0, "Enter Username")
root.mainloop()
