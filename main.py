#importing tkinter, PIL, pyglet, messagebox, random and string to my program to use
import tkinter as tk    #import the main GUI library to my program
from PIL import Image, ImageTk  #import Pillow to handle images
import pyglet   #import pyglet to use custom font
from tkinter import messagebox #import pop-up windows to use for error messages or info messages etc
import random #generate random choices, numbers, shuffle sequences
import string #load a standard Python library containing helpful string constants

#Global variables for my quiz
score = 0
current_index=0
all_questions= []
selected_choice= ""

#dictionary of questions, answer choices, answers and background image for that question
quiz_data = [
    {"question": "What planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars", "background": "Images/q1.png"},
    {"question": "What gas do humans need to breathe?", "choices": ["Carbon Dioxide", "Hydrogen", "Nitrogen", "Oxygen"], "answer": "Oxygen", "background": "Images/q2.png"},
    {"question": "Which organ pumps blood in the human body?", "choices": ["Brain", "Lungs", "Heart", "Kidney"],"answer": "Heart", "background": "Images/q3.png"},
    {"question": "Which state of matter has a fixed shape?", "choices": ["Liquid", "Gas", "Plasma", "Solid"], "answer": "Solid", "background": "Images/q4.png"},
    {"question": "Which blood cell carries oxygen?", "choices": ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "answer": "Red blood cells", "background": "Images/q5.png"},
    {"question": "What is friction mainly caused by?", "choices": ["Gravity", "Surface contact", "Magnetism", "Light"], "answer": "Surface contact", "background": "Images/q6.png"},
    {"question": "Which part of the cell controls activities?", "choices": ["Cytoplasm", "Nucleus", "Membrane", "Ribosome"], "answer": "Nucleus", "background": "Images/q7.png"},
    {"question": "Which part of the brain controls voluntary actions?", "choices": ["Cerebellum", "Neuron", "Brainstem", "Cerebrum"], "answer": "Cerebrum", "background": "Images/q8.png"},
    {"question": "Which energy transformation occurs in a moving car?", "choices": ["Chemical → kinetic", "Kinetic → chemical", "Thermal → light", "Light → sound"], "answer": "Chemical → kinetic", "background": "Images/q9.png"},
    {"question": "What is the main purpose of enzymes?","choices": ["Store energy", "Speed up reactions", "Carry oxygen", "Break bones"], "answer": "Speed up reactions", "background": "Images/q10.png"},
    {"question": "What is the name of radiation emitted by black holes?", "choices": ["Synchrotron", "Cherenkov", "Hawking radiation", "Bremsstrahlung"], "answer": "Hawking radiation", "background": "Images/q11.png"},
    {"question": "Which of the following is the SI unit of luminous intensity?", "choices": ["Lumen", "Lux", "Candela", "Watt"], "answer": "Candela", "background": "Images/q12.png"},
    {"question": "What is the rarest naturally occurring element on Earth?", "choices": ["Uranium", "Astatine", "Francium", "Rhodium"], "answer": "Astatine", "background": "Images/q13.png"},
    {"question": "Which protein maintains osmotic pressure in blood?", "choices": ["Gamma globulin", "Immunoglobulin", "Beta macroglobulin", "Albumin"], "answer": "Albumin", "background": "Images/q14.png"},
    {"question": "What is the powerhouse of the cell?", "choices": ["Nucleus", "Mitochondria", "Ribosome", "Membrane"], "answer": "Mitochondria", "background": "Images/q15.png"}
]

# Shuffle questions
random.shuffle(quiz_data)

#fonts
pyglet.font.add_file("fonts/Fredoka.ttf") #Load the font file from folder
pyglet.font.add_file("fonts/Agrandir.ttf")#Load the font file from folder

#intro window
root = tk.Tk() #create intro window
root.geometry("1225x690") #resize window
root.resizable(False, False) #make window unresizable
root.title("Quiz Homepage") #create a title for window
image = Image.open("Images/homepage.png") #open the background image file from the image folder
photo = ImageTk.PhotoImage(image) #convert image to a format so that tkinter can use
label = tk.Label(root, image=photo) #create a label widget to display the image
label.image = photo #keep reference to image
label.pack() #place the label onto the window

#start button
start_button = tk.PhotoImage(file="Images/startbutton.png") #load start button image
button = tk.Button(root, image=start_button, relief="flat", #put button in intro page, use the image of my start_button as the button and make the border of button have no 3D effect.
                   cursor="hand2",              #changes the cursor to a hand when reaches button
                   bg="#182156",                # Set colour to initial background colour
                   activebackground="#182156",  # Set colour active background colour to prevent flash when clicked
                   highlightthickness=0)        # Remove focus highlight around button
button.place(relx=0.5, rely=0.69, anchor="center") #position the button using coordinates and centre the button

#give button hover effects
def on_enter(event): #function for when user hovers over start button
    button.config(bg="#2b58a6") #colour changes to a lighter blue, letting users know the button is clickable

def on_leave(event): #function for when the user's cursor leaves start button
    button.config(bg="#182156") #colour changes to background colour to blend in

#linking buttons
button.bind("<Enter>", on_enter) #link mouse entry to previous function (on_enter)
button.bind("<Leave>", on_leave) #link mouse exit to previous function (on_leave)

#create label telling users to enter their username
outcome_label = tk.Label(root, text="Please Enter In Your Name", font=("Agrandir", 15, "bold")) #Ask user to enter their name
outcome_label.place(relx=0.5, rely=0.58, anchor="center") #position the label using coordinates and centre the label

#username validation
def check_username(): #function to check whether user enters a valid name
    username = username_entry.get() #retrieve user input

    if any(char.isdigit() for char in username): #check if users enters all numbers as their username
        outcome_label.config(text="You can not have numbers in your name", fg="red") #show red error message telling users they can't have numbers in their name
    elif username.strip() == "": #check if users enters nothing
        outcome_label.config(text="Please enter a name", fg="red") #show red error message for empty name
    elif any(char in "!@#$%^&*()-_=+~[]{}|;:'\",<.>/?\\" for char in username): #check if users enter in special characters
        outcome_label.config(text="No special characters allowed", fg="red") #show red error message telling users they can't have special characters in their name
    else:
        outcome_label.config(text=f"Welcome to the quiz, {username}!", fg="green") #welcome users in green if user enters a valid name
        root.after(1750, open_next_window) #wait 1.75 seconds before heading to next window

#create username entry box
username_entry = tk.Entry(root, font=("Arial", 15), bd=2.5, width=25) #create an entry box for users to enter their name
username_entry.place(relx=0.5, rely=0.52, anchor="center") #position the box using coordinates and centre the box
button.config(command=check_username) #check username for the function
username_entry.bind('<Return>', lambda event: check_username()) #allow users to click enter on their keyboard when entering in a name

#main window/questions window
def open_next_window(): #create next window
    global selected_choice  #global variable
    new_window = tk.Toplevel(root) #create a pop-up window
    new_window.title("Quiz Main Questions Page") #assign a name to window
    new_window.geometry("1225x690") #resize window
    new_window.resizable(False, False) #make window unresizable

    #background
    bg_image = Image.open("Images/q1.png") #open background image for first question
    bg_photo = ImageTk.PhotoImage(bg_image) #convert image to a format tkinter can use
    bg_label = tk.Label(new_window, image=bg_photo) #create a label widget to display background image
    bg_label.image = bg_photo #reference image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) #pins the top-left corner of the label to the exact top-left corner of new window and set the width and height of the label relative to the parent window

    #create a label to display question
    question_label = tk.Label(  #name label
        new_window, #put label in new_window
        text="Question 1", #text
        font=("Fredoka", 25, "bold"), #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        wraplength=600 #automatically break the text into a new line if it exceeds 600 pixels in width
    )

    #place the label at an suitable coordinate
    question_label.place(x=285, y=35, width=600, height=80)

    #create a progress label to display what question the user is currently at
    progress_label = tk.Label(  #name label
        new_window, #put label in new_window
        text=f"1/{len(quiz_data)}", #text of progress
        font=("Fredoka", 35, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white"  #set label background colour to white
    )

    #place the label at an suitable coordinate
    progress_label.place(x=58, y=43, width=120, height=70)

    #create a exit button
    exit_btn = tk.Button(   #name button
        new_window, #put button in new_window
        text="QUIT",    #text
        font=("Fredoka", 25, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = root.destroy #end code
    )

    #place the button at an suitable coordinate
    exit_btn.place(x=148, y=255, width=120, height=70)

    global selected_choice, current_selected_button
    selected_choice = None #Define the variable to prevent errors on startup before any button is clicked
    current_selected_button = None #Define the variable to prevent errors on startup before any button is clicked

    #create first answer button
    answer1 = tk.Button( #name answer button
        new_window, #put button in new_window
        text="Answer 1",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer1["text"], answer1) #run the selected answer with the following def command
    )

    #place the button  at an suitable coordinate
    answer1.place(x=202, y=416, width=325, height=59)

    #create second answer button
    answer2 = tk.Button(    #name answer button
        new_window, #put button in new_window
        text="Answer 2",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer2["text"], answer2) #run the selected answer with the following def command
    )

    # place the button  at an suitable coordinate
    answer2.place(x=661, y=416, width=325, height=59)

    #create third answer button
    answer3 = tk.Button(    #name answer button
        new_window, #put button in new_window
        text="Answer 3",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer3["text"], answer3) #run the selected answer with the following def command
    )

    # place the button  at an suitable coordinate
    answer3.place(x=202, y=567, width=325, height=58)

    #create fourth answer button
    answer4 = tk.Button(    #name answer button
        new_window, #put button in new_window
        text="Answer 4",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer4["text"], answer4) #run the selected answer with the following def command
    )

    # place the button  at an suitable coordinate
    answer4.place(x=661, y=567, width=324, height=58)

    # Answer Selection Function
    def select_answer(choice, clicked_button):  #create def function
        global selected_choice, current_selected_button   #keep track of choice and button selection
        selected_choice = choice   #name selected_choice
        current_selected_button = clicked_button #record what button was clicked

        # Reset colours
        answer1.config(bg="white")  #set initial background colour of button to white
        answer2.config(bg="white")  #set initial background colour of button to white
        answer3.config(bg="white")  #set initial background colour of button to white
        answer4.config(bg="white")  #set initial background colour of button to white

        clicked_button.config(bg="#708090") #change colour of button when clicked

    #Put the questions, answer choices and background onto the page
    def load_question():
        global current_index
        question = quiz_data[current_index] #load question from dictionary
        global current_selected_button

        current_selected_button = None  #set current selected button as none

        answer1.config(bg="white")  #reset colour of button
        answer2.config(bg="white")  #reset colour of button
        answer3.config(bg="white")  #reset colour of button
        answer4.config(bg="white")  #reset colour of button

        question_label.config(text=question["question"]) # Update question text for my question label
        answer1.config(text=question["choices"][0])  # Update answer buttons
        answer2.config(text=question["choices"][1])  # Update answer buttons
        answer3.config(text=question["choices"][2])  # Update answer buttons
        answer4.config(text=question["choices"][3])  # Update answer buttons

        progress_label.config( #adjust progress label
        text=f"{current_index + 1}/{len(quiz_data)}" ) # Update progress label for each question

        #Update background image for each question
        new_bg = Image.open(question["background"]) #use the Pillow library (PIL) to load image and fetch questions in the dictionary
        new_bg_photo = ImageTk.PhotoImage(new_bg) #Converts the Pillow image into a PhotoImage object ( a format Tk can use)
        bg_label.config(image=new_bg_photo) #Changes the image property of an existing label named bg_label so now image instantly appears on screen
        bg_label.image = new_bg_photo #keep reference of image
    #function for submitting answer
    def submit_answer():    #create def function
        global current_index
        global score
        global selected_choice

        # Make sure an answer was chosen through error box
        if selected_choice is None: #if user doesn't select an button
            messagebox.showwarning( #create an error box
                "You have not selected an Answer",   #text of title
                "Please select an answer first before submitting, even if it is just a guess :)"   #message telling user to select an answer
            )
            return #return back

        # Check answer
        correct_answer = quiz_data[current_index]["answer"] #check answer from dictionary
        if selected_choice == correct_answer:   #check if the selected answer from user matches the correct answer
            score += 1  #add a point

        # Next question
        current_index += 1  #add 1 to index for progress

        # Reset selection
        selected_choice = None  #reset selected choice

        # Check if quiz is done
        if current_index >= len(quiz_data): #check if all questions were asked in the dictionary
            new_window.destroy()    #close new window

        else:   #else
            load_question() #otherwise load next question

    #create a submit button
    submit_btn = tk.Button(     #name button
        new_window, #put button in new_window
        text="SUBMIT",  #text
        font=("Fredoka", 25, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command=submit_answer
    )

    #place the button at an suitable coordinate
    submit_btn.place(x=905, y=255, width=125, height=70)

    # hover functions for buttons in new_window
    def on_enter(event):    #create def function for when user hovers over a button
        global current_selected_button
        # Only show light gray hover if the button is not  the selected one
        if event.widget != current_selected_button:
            event.widget.config(bg="#D6D6D6", fg="black")

    def on_leave(event):    #create def function for when user hovers away from a button
        global current_selected_button
        # Only revert to white if the button is not the selected one
        if event.widget != current_selected_button:
            event.widget.config(bg="white", fg="black")

    # bind all the buttons in the new_window and applying hover effects
    for widget in new_window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

    load_question()
    root.withdraw() #hide the window

root.mainloop() #run the loop to keep window open
