import tkinter as tk #import the main GUI library to my program
from PIL import Image, ImageTk #import Pillow to handle images
import pyglet #import pyglet to use custom font
from tkinter import messagebox
#Global variables for my quiz
score = 0
current_index=0
all_questions= []
selected_choice= ""
#dictionary of questions, answer choices, answers and background image for that question
quiz_data = [
        {"question": "What planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars", "background": "Images/q1.png"},
    {"question": "What gas do humans need to breathe?", "choices": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Oxygen", "background": "Images/q2.png"},
    {"question": "Which organ pumps blood in the human body?", "choices": ["Brain", "Lungs", "Heart", "Kidney"],"answer": "Heart", "background": "Images/q3.png"},
    {"question": "Which state of matter has a fixed shape?", "choices": ["Liquid", "Gas", "Solid", "Plasma"], "answer": "Solid", "background": "Images/q4.png"},
    {"question": "Which blood cell carries oxygen?", "choices": ["White blood cells", "Red blood cells", "Platelets", "Plasma"], "answer": "Red blood cells", "background": "Images/q5.png"},
    {"question": "What is friction mainly caused by?", "choices": ["Gravity", "Surface contact", "Magnetism", "Light"], "answer": "Surface contact", "background": "Images/q6.png"},
    {"question": "Which part of the cell controls activities?", "choices": ["Cytoplasm", "Nucleus", "Membrane", "Ribosome"], "answer": "Nucleus", "background": "Images/q7.png"},
    {"question": "Which part of the brain controls voluntary actions?", "choices": ["Cerebellum", "Cerebrum", "Brainstem", "Neuron"], "answer": "Cerebrum", "background": "Images/q8.png"},
    {"question": "In the Heisenberg uncertainty principle, position and momentum cannot be observed precisely at the same time?", "choices": ["Velocity and Acceleration", "Mass and Energy", "Position and Momentum", "Spin and Charge"], "answer": "Position and Momentum", "background": "Images/q9.png"},
    {"question": "What is the main purpose of enzymes?","choices": ["Store energy", "Speed up reactions", "Carry oxygen", "Break bones"], "answer": "Speed up reactions", "background": "Images/q10.png"},
    {"question": "What is the name of radiation emitted by black holes?", "choices": ["Synchrotron", "Hawking radiation", "Cherenkov", "Bremsstrahlung"], "answer": "Hawking radiation", "background": "Images/q11.png"},
    {"question": "Which of the following is the SI unit of luminous intensity?", "choices": ["Lumen", "Lux", "Candela", "Watt"], "answer": "Candela", "background": "Images/q12.png"},
    {"question": "What is the rarest naturally occurring element on Earth?", "choices": ["Uranium", "Astatine", "Francium", "Rhodium"], "answer": "Astatine", "background": "Images/q13.png"},
    {"question": "Which protein maintains osmotic pressure in blood?", "choices": ["Gamma globulin", "Immunoglobulin", "Beta macroglobulin", "Albumin"], "answer": "Albumin", "background": "Images/q14.png"},
    {"question": "What is the powerhouse of the cell?", "choices": ["Nucleus", "Mitochondria", "Ribosome", "Membrane"], "answer": "Mitochondria", "background": "Images/q15.png"}
]
pyglet.font.add_file("fonts/Fredoka.ttf") #Load the font file from folder
pyglet.font.add_file("fonts/Agrandir.ttf")#Load the font file from folder
root = tk.Tk() #create intro window
root.geometry("1225x690") #resize window
root.resizable(False, False) #make window unresizable
root.title("Quiz Homepage") #create a title for window
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

outcome_label = tk.Label(root, text="Please Enter In Your Name", font=("Agrandir", 15, "bold")) #Ask user to enter their name
outcome_label.place(relx=0.5, rely=0.58, anchor="center") #position the label using coordinates and centre the label
def check_username(): #function to check whether user enters a valid name
    username = username_entry.get() #retrieve user input

    if any(char.isdigit() for char in username): #check if users enters all numbers as their username
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
    new_window.geometry("1225x690") #resize window
    new_window.resizable(False, False) #make window unresizable

    bg_image = Image.open("Images/q1.png") #open background image for first question
    bg_photo = ImageTk.PhotoImage(bg_image) #convert image to a format tkinter can use
    bg_label = tk.Label(new_window, image=bg_photo) #create a label widget to display background image
    bg_label.image = bg_photo #reference image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    #create a label to display question
    question_label = tk.Label(
        new_window,
        text="Question 1",
        font=("Fredoka", 50, "bold"),
        fg="black",
        bg="white",
    )
    #place the label at an suitable coordinate
    question_label.place(x=285, y=35, width=600, height=80)
    #create a progress label to display what question the user is currently at
    progress_label = tk.Label(
        new_window,
        text="1/30",
        font=("Fredoka", 42, "bold"),
        fg="black",
        bg="white"
    )
    #place the label at an suitable coordinate
    progress_label.place(x=58, y=43, width=120, height=70)
    #create a exit button
    exit_btn = tk.Button(
        new_window,
        text="QUIT",
        font=("Fredoka", 25, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    #place the button at an suitable coordinate
    exit_btn.place(x=158, y=255, width=100, height=70)
    #create a submit button
    submit_btn = tk.Button(
        new_window,
        text="SUBMIT",
        font=("Fredoka", 25, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    #place the button at an suitable coordinate
    submit_btn.place(x=905, y=255, width=120, height=70)
    #create first answer button
    answer1 = tk.Button(
        new_window,
        text="Answer 1",
        font=("Fredoka", 18, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    #place the button  at an suitable coordinate
    answer1.place(x=202, y=416, width=322, height=58)
    #create second answer button
    answer2 = tk.Button(
        new_window,
        text="Answer 2",
        font=("Fredoka", 18, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    # place the button  at an suitable coordinate
    answer2.place(x=660, y=416, width=322, height=58)
    #create third answer button
    answer3 = tk.Button(
        new_window,
        text="Answer 3",
        font=("Fredoka", 18, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    # place the button  at an suitable coordinate
    answer3.place(x=202, y=567, width=322, height=58)
    #create fourth answer button
    answer4 = tk.Button(
        new_window,
        text="Answer 4",
        font=("Fredoka", 18, "bold"),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2"
    )
    # place the button  at an suitable coordinate
    answer4.place(x=660, y=567, width=322, height=58)



    root.withdraw() #hide the window

root.mainloop() #run the loop to keep window open
