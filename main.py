import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
image = Image.open("Images/homepage.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

def open_next_window():
    new_window = tk.Toplevel(root)
    new_window.title("Quiz Main Questions Page")
    next_img = Image.open("Images/page1.png")
    next_photo = ImageTk.PhotoImage(next_img)
    img_label = tk.Label(new_window, image=next_photo)
    img_label.image = next_photo
    img_label.pack(pady=10)
    root.withdraw()

start_button = tk.PhotoImage(file="Images/startbutton.png")
button = tk.Button(root, image=start_button, relief="flat", cursor="hand2")
button.place(relx=0.5, rely=0.69, anchor="center")

def on_enter(event):
    button.config(bg="#2b58a6")

def on_leave(event):
    button.config(bg="#182156")

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

outcome_label = tk.Label(root, text="", font=("Arial", 15))
outcome_label.place(relx=0.5, rely=0.59, anchor="center")
def check_username():
    username = username_entry.get()

    if username.isdigit():
        outcome_label.config(text="You can not have numbers in your name", fg="red")
    elif username.strip() == "":
        outcome_label.config(text="Please enter a name", fg="red")
    elif any(char in "!@#$%^&*()-_=+~[]{}|;:'\",<.>/?\\" for char in username):
        outcome_label.config(text="No special characters allowed", fg="red")
    else:
        outcome_label.config(text=f"Welcome to the quiz, {username}!", fg="green")
        root.after(2000, open_next_window)

username_entry = tk.Entry(root, font=("Arial", 15), bd=2.5, width=25)
username_entry.place(relx=0.5, rely=0.54, anchor="center")
button.config(command=check_username)

root.mainloop()
