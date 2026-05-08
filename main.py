import tkinter as tk #import the main GUI library to my program
from PIL import Image, ImageTk #import Pillow to handle images

root = tk.Tk() #create intro window
image = Image.open("Images/homepage.png") #open the background image file from the image folder
photo = ImageTk.PhotoImage(image) #convert image to a format so that tkinter can use
label = tk.Label(root, image=photo) #create a label widget to display the image
label.image = photo #keep reference to image
label.pack() #place the label onto the window
start_button = tk.PhotoImage(file="Images/startbutton.png") #load start button image
button = tk.Button(root, image=start_button, relief="flat",
                   cursor="hand2",              #changes the cursor to a hand when reaches button
                   bg="#182156",                # Set colour to initial background colour
                   activebackground="#182156",  # Set colour active background colour to prevent flash when clicked
                   highlightthickness=0)        # Remove focus highlight around button
button.place(relx=0.5, rely=0.69, anchor="center") #position the button using coordinates and centre the button

def on_enter(event): #function for when user hovers over start button
    button.config(bg="#2b58a6") #colour changes to a lighter blue, letting users know the button is clickable

def on_leave(event): #function for when the user's cursor leaves start button
    button.config(bg="#182156") #colour changes to background colour to blend in

button.bind("<Enter>", on_enter) #link mouse entry to previous function (on_enter)
button.bind("<Leave>", on_leave) #link mouse exit to previous function (on_leave)

outcome_label = tk.Label(root, text="Please Enter In Your Name", font=("Arial", 15)) #Ask user to enter their name
outcome_label.place(relx=0.5, rely=0.58, anchor="center") #position the label using coordinates and centre the label
def check_username(): #function to check whether user enters a valid name
    username = username_entry.get() #retrieve user input

    if username.isdigit() #check if users enters all numbers as their username
        outcome_label.config(text="You can not have numbers in your name", fg="red") #show error message telling users they can't have numbers in their name
    elif username.strip() == "": #check if users enters nothing
        outcome_label.config(text="Please enter a name", fg="red") #show error message for empty name
    elif any(char in "!@#$%^&*()-_=+~[]{}|;:'\",<.>/?\\" for char in username): #check if users enter in special characters
        outcome_label.config(text="No special characters allowed", fg="red") #show error message telling users they can't have special characters in their name
    else:
        outcome_label.config(text=f"Welcome to the quiz, {username}!", fg="green") #welcome users if user enters a valid name
        root.after(1750, open_next_window) #wait 1.75 seconds before heading to next window

username_entry = tk.Entry(root, font=("Arial", 15), bd=2.5, width=25) #create an entry box for users to enter their name
username_entry.place(relx=0.5, rely=0.52, anchor="center") #position the box using coordinates and centre the box
button.config(command=check_username) #check username for the function

def open_next_window(): #create next window
    new_window = tk.Toplevel(root) #create a pop-up window
    new_window.title("Quiz Main Questions Page") #assign a name to window
    next_img = Image.open("Images/q1.png") #opem background image
    next_photo = ImageTk.PhotoImage(next_img)
    img_label = tk.Label(new_window, image=next_photo)
    img_label.image = next_photo
    img_label.pack(pady=10)





    root.withdraw()

root.mainloop()
