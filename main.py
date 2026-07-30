#importing tkinter, PIL, pyglet, messagebox, random and string to my program to use
import tkinter as tk    #import the main GUI library to my program
from PIL import Image, ImageTk  #import Pillow to handle images
import pyglet   #import pyglet to use custom font
from tkinter import messagebox #import pop-up windows to use for error messages or info messages etc
import random #generate random choices, numbers, shuffle sequences
import string #load a standard Python library containing helpful string constants

#Global variables for my quiz
score = 0 #set score as 0
current_index=0 #set progress as 0
selected_choice= None  #reset user's selected choice
warning_is_open = False #set variable to false
info_is_open = False    #set variable to false
username = "" #set username as empty space to be able to use variable later

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
button = tk.Button(root, image=start_button, relief="flat", #create and name button, put button in intro page, use the image of my start_button as the button and make the border of button have no 3D effect.
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
outcome_label = tk.Label(root, text="Please Enter In Your Name", font=("Agrandir", 15, "bold")) #create and name label, place in start page, ask user to enter their name, change font, font size and make bold
outcome_label.place(relx=0.5, rely=0.58, anchor="center") #position the label using coordinates and centre the label

#username validation
def check_username(): #function to check whether user enters a valid name
    global username #keep track of username to use in the end window
    username = username_entry.get() #retrieve user input

    if any(char.isdigit() for char in username): #check if users enters all numbers as their username
        outcome_label.config(text="You can not have numbers in your name", fg="red") #show red error message telling users they can't have numbers in their name
    elif username.strip() == "": #check if users enters nothing
        outcome_label.config(text="Please enter a name", fg="red") #show red error message for empty name
    elif any(char in "!@#$%^&*()-_=+~[]{}|;:'\",<.>/?\\" for char in username): #check if users enter in special characters
        outcome_label.config(text="No special characters allowed", fg="red") #show red error message telling users they can't have special characters in their name
    else:
        outcome_label.config(text=f"Welcome to the quiz, {username}!", fg="green") #welcome users in green if user enters a valid name
        button.config(command=lambda: None) #disables the button after the user has clicked it once to prevent multiple new windows from opening.
        root.after(1500, open_next_window) #wait 1.5 seconds before heading to next window

#create username entry box
username_entry = tk.Entry(root, font=("Arial", 15), bd=2.5, width=25) #create and name entry box for users to enter their name
username_entry.place(relx=0.5, rely=0.52, anchor="center") #position the box using coordinates and centre the box
button.config(command=check_username) #check username for the function
username_entry.bind('<Return>', lambda event: check_username()) #allow users to click enter on their keyboard when entering in a name

#main window/questions window
def open_next_window(): #create next window
    global selected_choice  #global variable to keep track of selected_choice
    global current_index, score #global variable to keep track of current question number and score
    global new_window #set as global variable
    global warning_is_open #global variable to be able to use variable
    global info_is_open #global variable to be able to use variable
    current_index = 0 #Reset the current question number back to 0
    score = 0 #reset score back to 0
    new_window = tk.Toplevel(root) #create a pop-up window
    new_window.title("Quiz Main Questions Page") #assign a name to window
    new_window.geometry("1225x690") #resize window
    new_window.resizable(False, False) #make window unresizable

    #background for questions page
    bg_image = Image.open("Images/q1.png") #open background image for first question
    bg_photo = ImageTk.PhotoImage(bg_image) #convert image to a format tkinter can use
    bg_label = tk.Label(new_window, image=bg_photo) #create a label widget to display background image
    bg_label.image = bg_photo # keep reference of image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) #pins the top-left corner of the label to the exact top-left corner of new window and set the width and height of the label relative to the parent window

    #create a label to display question
    question_label = tk.Label(  #create and name label
        new_window, #put label in new_window
        text="Question 1", #text
        font=("Fredoka", 28, "bold"), #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        wraplength=600 #automatically break the text into a new line if it exceeds 600 pixels in width
    )

    #place the label at an suitable coordinate
    question_label.place(x=285, y=35, width=600, height=80)

    #create a progress label to display what question the user is currently at
    progress_label = tk.Label(  #create and name label
        new_window, #put label in new_window
        text=f"1/{len(quiz_data)}", #text of progress
        font=("Fredoka", 35, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white"  #set label background colour to white
    )

    # place the label at an suitable coordinate
    progress_label.place(x=56, y=43, width=120, height=70)

    #create a current score label to display how many correct answers the user has gotten
    current_score_label = tk.Label( #create and name label
        new_window,  #put label in new_window
        text="Score: 0", #text showing current score starting with 0 which will be updated
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        bg="white"  #set label background colour to white
    )

    # place the label at an suitable coordinate
    current_score_label.place(relx=0.07, rely=0.28, anchor="center")

    #Def function for preventing accidentally clicking exit button by adding confirmation button
    def quit_quiz():    #create def function
        global warning_is_open  #use global variable to be able to use warning_is_open

        # If a warning is already on screen, exit immediately
        if warning_is_open:
            return  # return back

        # Set lock to True before showing the following message box
        warning_is_open = True
        answer = messagebox.askyesno(   #create confirmation messagebox
            "Exit Quiz Confirmation",    #title
            "Are you sure you want to quit?\n\n"    #text
                    "If so, feel free to come back anytime!",   #text
                    parent = new_window) #pin messagebox on top of my main game window

        if answer:  #if yes
            root.destroy()  #end code by destroying window

        # Reset lock to False only after the user closes/exits the message box
        warning_is_open = False

    #create a exit button
    exit_btn = tk.Button(   #create and name button
        new_window, #put button in new_window
        text="QUIT",    #text
        font=("Fredoka", 25, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = quit_quiz #show confirmation messagebox from quit_quiz def function
    )

    #place the button at an suitable coordinate
    exit_btn.place(x=148, y=255, width=120, height=70)

    global selected_choice, current_selected_button #keep track of selected_choice and current_selected_button
    selected_choice = None #Define the variable to prevent errors on startup before any button is clicked
    current_selected_button = None #Define the variable to prevent errors on startup before any button is clicked

    #create first answer button
    answer1 = tk.Button( #create and name answer button
        new_window, #put button in new_window
        text="Answer 1",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer1["text"], answer1) #run the selected answer with the following def command to see if answer is correct or incorrect
    )

    #place the button at an suitable coordinate
    answer1.place(x=202, y=416, width=325, height=59)

    #create second answer button
    answer2 = tk.Button(    #create and name answer button
        new_window, #put button in new_window
        text="Answer 2",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer2["text"], answer2) #run the selected answer with the following def command to see if answer is correct or incorrect
    )

    # place the button  at an suitable coordinate
    answer2.place(x=661, y=416, width=325, height=59)

    #create third answer button
    answer3 = tk.Button(    #create and name answer button
        new_window, #put button in new_window
        text="Answer 3",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer3["text"], answer3) #run the selected answer with the following def command to see if answer is correct or incorrect
    )

    # place the button  at an suitable coordinate
    answer3.place(x=202, y=567, width=325, height=58)

    #create fourth answer button
    answer4 = tk.Button(    #create and name answer button
        new_window, #put button in new_window
        text="Answer 4",    #text
        font=("Fredoka", 18, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command = lambda: select_answer(answer4["text"], answer4) #run the selected answer with the following def command to see if answer is correct or incorrect
    )

    # place the button  at an suitable coordinate
    answer4.place(x=661, y=567, width=324, height=58)

    #create a pop up to help users better understand how quiz works
    def helpbox():   #create def function
        global info_is_open
        # If a warning is already on screen, exit immediately
        if info_is_open:
            return #return back

        # Set lock to True before showing the following message box
        info_is_open = True

        messagebox.showinfo(    #create  info messagebox
            "Quiz Info\n\n",  # text of title
                    "- Welcome to my Science Quiz!\n\n" #messages
            "- For each question, select one answer from the 4 answer choices.\n\n" #messages
            "- Press the next button to submit your answer and move on to the next question.\n\n" #messages
            "- You cannot change your answer after it has been submited, so ensure the answer you choose before submitting is your final answer.\n\n" #messages
            "- There are 15 questions in total.\n\n" #messages
            "- You need to get at least 9 out of 15 questions correct (which is 60%) to pass the quiz.\n\n" #messages
            "- If you don't feel like playing or want to restart, feel free to press the exit button. This ends the code.\n\n" #messages
            "- Good luck and have fun learning new things!\n\n",   #messages
        parent=new_window)  #pin messagebox on top of my main game window

        # Reset lock to False only after the user closes/exits the message box
        info_is_open = False
        return   #return

    #Info button
    info_image = Image.open("Images/info.png") #open the image from folder
    info_image = info_image.resize((100, 60))   #resize the image to an appriopiate size
    info_photo = ImageTk.PhotoImage(info_image) #load info button image

    info_button = tk.Button(    #create and name button
        new_window, #place in new window
        image=info_photo,   #use the image as the button
        command=helpbox,    #head to the helpbox def function to show messagebox
        relief="flat",      #removes all 3D borders and shadowing from button
        cursor="hand2",     #change cursor to hand to let users know this button is clickable
        bg = "white",  # Set colour to initial background colour
        activebackground = "#182156",  # Set colour active background colour to prevent flash when clicked
        highlightthickness = 0  # Remove focus highlight around button
    )
    info_button.image = info_photo  #keep reference to image
    info_button.place(relx=0.17, rely=0.28, anchor="center")  # place button at a suitable coordinate

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
    def load_question():    #create def function
        global current_index    #keep track of current question number
        question = quiz_data[current_index] #load question from dictionary
        global current_selected_button  #keep track of current_selected_button
        current_selected_button = None  #set current selected button as none
        global button_map   #enable button_map

        #Hide feedback message to avoid being in the way
        feedback_label.place_forget()

        #shuffle choices around to prevent users from just memorising which button contains the answers if they were to play the quiz again
        choices = question["choices"][:]
        random.shuffle(choices)
        answer1.config(text=choices[0])
        answer2.config(text=choices[1])
        answer3.config(text=choices[2])
        answer4.config(text=choices[3])

        #answer button colour
        answer1.config(bg="white")  #reset colour of button back to white
        answer2.config(bg="white")  #reset colour of button back to white
        answer3.config(bg="white")  #reset colour of button back to white
        answer4.config(bg="white")  #reset colour of button back to white

        #enable buttons
        answer1.config(state="normal")  #enable answer 1 button to be clickable
        answer2.config(state="normal")  #enable answer 2 button to be clickable
        answer3.config(state="normal")  #enable answer 3 button to be clickable
        answer4.config(state="normal")  #enable answer 4 button to be clickable

        #update question label and the four answer buttons
        question_label.config(text=question["question"]) # Update question text for my question label

        #update progress
        progress_label.config( #adjust progress label
        text=f"{current_index + 1}/{len(quiz_data)}" ) # Update progress label for each question

        #update current score
        current_score_label.config(text=f"Score: {score}")  #update score for each correct answer

        #Update background image for each question
        new_bg = Image.open(question["background"]) #use the Pillow library (PIL) to load image and fetch questions in the dictionary
        new_bg_photo = ImageTk.PhotoImage(new_bg) #Converts the Pillow image into a PhotoImage object ( a format Tk can use)
        bg_label.config(image=new_bg_photo) #Changes the image property of an existing label named bg_label so now image instantly appears on screen
        bg_label.image = new_bg_photo #keep reference of image

        #dictionary called Button map which will help change the colour of the answer the user has selected
        button_map = {
            answer1["text"]: answer1,
            answer2["text"]: answer2,
            answer3["text"]: answer3,
            answer4["text"]: answer4}

        #function for submitting answer
    def submit_answer():    #create def function
        #global variables that are needed
        global current_index    #use and keep track of progress
        global score    #use and keep track of score
        global selected_choice  #use
        global warning_is_open  #use

        # place the label at an suitable coordinate
        feedback_label.place(x=575, y=325, anchor="center")

        # Make sure an answer was chosen through an error message box
        if selected_choice is None: #if user doesn't select an button

            # If a warning is already on screen, exit immediately
            if warning_is_open:
                return  #return back

            # Set lock to True before showing the following message box
            warning_is_open = True

            messagebox.showwarning( #create an error box
                "You have not selected an Answer",   #text of title
                "Please select an answer first before submitting, even if it is just a guess :)",   #message telling user to select an answer
            parent=new_window   #keep this on top of new_window
            )
            # Reset lock to False only after the user closes/exits the message box
            warning_is_open = False
            return #return back

        # Check answer
        correct_answer = quiz_data[current_index]["answer"] #check answer from dictionary
        if selected_choice == correct_answer:   # if the selected answer from user matches the correct answer
            score += 1  #add a point to score

            feedback_label.config(  #show label for feedback
                text=f"Keep it up, you have answered correctly!",    #words of encouragement
                fg="green", #make text green
                bg="#FDFD96"),    #make background pastel yellow


        else:
            feedback_label.config(  #show label for feedback
                text=f" Good try but Incorrect!\nThe answer was: {correct_answer}",     #words of encouragement
                fg="red",   #make text red
                bg="#FDFD96", )   #make background pastel yellow

        #Changing answer buttons
        # Colour the chosen answer red if incorrect
        if selected_choice != correct_answer:   #if answer is incorrect
            button_map[selected_choice].config(bg="#ff6b6b")    #change to red

        # Colour the correct answer green
        button_map[correct_answer].config(bg="#7CFC00") #change to green

        #disable changing colour
        answer1.config(state="disabled")    #disable colour answer 1
        answer2.config(state="disabled")    #disable colour answer 2
        answer3.config(state="disabled")    #disable colour answer 3
        answer4.config(state="disabled")    #disable colour answer 4

        #next question function
        def next_question():    #create def function
            global current_index, selected_choice   #add current_index and selected_choice to be able to use them

            current_index += 1  #update progress
            selected_choice = None  #reset selected choice so user can select an answer button

            #feedback label
            feedback_label.config(text="")  #change text

            # Check if quiz is done
            if current_index >= len(quiz_data): #check if all questions were asked in the dictionary
                new_window.destroy()    #close new window
                show_results()  #go to results page
            else:   #else
                load_question() #otherwise load next question

        #head to next question after 1000ms (1 second)
        new_window.after(1000,next_question)

    #create a submit button
    submit_btn = tk.Button(     #create and name button
        new_window, #put button in new_window
        text="SUBMIT",  #text
        font=("Fredoka", 25, "bold"),   #font and size of the text and make text bold
        fg="black", #set text colour to back
        bg="white", #set label background colour to white
        relief="flat",  #removes all 3D borders and shadowing from button
        cursor="hand2",  #change cursor to hand to let users know this button is clickable
        command=submit_answer   #run the command of a submit button
    )
    #create a label to tell user whether they answered a question correct or not
    feedback_label = tk.Label( #create label and name it feedback_label
        new_window, #place in new_window
        text="",    #put text as nothing which will be replaced later by either a "correct" or an "incorrect" depending on whether user has answered correctly
        font=("Fredoka", 18, "bold"),   #make font Fredoka to maintain consistency and make text bold and large enough to be seen by my users
    )
    #place the label at an suitable coordinate
    feedback_label.place(x=575, y=325, anchor="center")

    #place the button at an suitable coordinate
    submit_btn.place(x=905, y=255, width=125, height=70)

    # hover functions for buttons in new_window
    def on_enter(event):    #create def function for when user hovers over a button
        global current_selected_button
        # Only show light gray hover if the button is not  the selected one
        if event.widget != current_selected_button:
            event.widget.config(bg="#D6D6D6", fg="black")   #change colour

    def on_leave(event):    #create def function for when user hovers away from a button
        global current_selected_button
        # Only revert to white if the button is not the selected one
        if event.widget != current_selected_button:
            event.widget.config(bg="white", fg="black") #change colour

    # bind all the buttons in the new_window and applying hover effects
    for widget in new_window.winfo_children():
        if isinstance(widget, tk.Button):   #if it is a widget or button
            widget.bind("<Enter>", on_enter)    #bind button
            widget.bind("<Leave>", on_leave)    #bind button

    load_question() #load question

    #End page (win or lose)
    def show_results(): #create def function
        global warning_is_open  #to be able to use warning_is_open
        global score    #to be able to use score
        result_window = tk.Toplevel(root)   #create a pop-up window
        result_window.title("Results Page") #create title
        result_window.geometry("1225x690")  #resize window
        result_window.resizable(False, False) #make window unresizeable

        #Opening background
        if score >= 9: #if user scores 9 or more
            image = Image.open("Images/winpage.png")    #open win page
        else:   #otherwise
            image = Image.open("Images/losepage.png")   #open lose page

        #background images for win/lose page
        photo = ImageTk.PhotoImage(image)   #convert image to a format tkinter can use
        label = tk.Label(result_window, image=photo)    #create a label widget to display background image
        label.image = photo #keep reference of image
        label.pack()    #positions image

        # dictionary random messages of positive feedback
        positive_messages = [
            "Amazing work!",
            "Fantastic effort!",
            "Outstanding!",
            "Excellent job!",
            "You're a science superstar!",
            "Your hard work and dedication definitely show off with this score!",
            "You nailed the tricky questions on this quiz, that shows you really understand the material!",
            "Exceptional critical thinking!",
            "You absolutely crushed it!",
            "High five! You did well",
            "You should be so proud of what you've learned. You're ready for whatever comes next!"
        ]

        # dictionary random messages of negative feedback
        negative_messages = [
            "Good effort!",
            "Keep practising!",
            "You'll do even better next time!",
            "Don't give up!",
            "Hope you’ve learnt something new!",
            "This quiz was tough, but I am really proud of how hard you tried.",
            "Mistakes are just proof that you are trying. Let's look at what we can learn from them.",
            "A low score just means you are in the middle of learning something new. Keep going!",
            "Your score today doesn't define how smart you are. It just shows where we need to start next time.",
            "Every expert started right where you are now. Let's dust ourselves off and try again.",
            "Everyone has bad days, and that is completely okay.",
            "The best way to grow your brain is by making mistakes and fixing them. You're on the right track.",
        ]
        #postive and negative messages
        if score >= 9:  # if user scores 9 or more
            message = random.choice(positive_messages)  #print random positive message
            text_colour = "#1B5E20"  #make text Dark green
        else:  # otherwise
            message = random.choice(negative_messages)  #print random negative message
            text_colour = "#C62828"  # make text Dark red

        # Display the positive or negative message
        message_label = tk.Label(   #create and name label using tkinter
            result_window,  #place in end window
            text=message,   #print random positive or negative image depending on users score
            wraplength=600,  # automatically break the text into a new line if it exceeds 100 pixels in width
            font=("Fredoka", 17, "bold"),   #change font to Fredoka, make font size 18, make bold
            bg="white", #make background white
            fg=text_colour  #make font colour depending on user score
        )
        # place label at an suitable coordinate
        message_label.place(x=525, y=90, width=800, height=100, anchor="center")


        #show user their score
        score_label = tk.Label( #create and name label
            result_window,  #place in result_window
            text=f"{score}/{len(quiz_data)}",   #text
            font=("Fredoka", 35, "bold"),    #font, font size, make bold
            bg="white", #set background to white
            activebackground = "#182156",   #set active background to dark blue
            highlightthickness = 0, #remove highlight thickness
            relief="flat"   #   #removes all 3D borders and shadowing from label
        )

        # place label at an suitable coordinate
        score_label.place(relx=0.35, rely=0.675, anchor="center", width=120, height=80)

        #show percentage score
        percentage_label= tk.Label( #create and name percentage label using tkinter
            result_window,  # place in result_window
            font=("Fredoka", 35, "bold"),  # font, font size, make bold
            bg="white",  # set background to white
            activebackground="#182156",  # set active background to dark blue
            highlightthickness=0,  # remove highlight thickness
            relief="flat",  # #removes all 3D borders and shadowing from label
            text=f"{(score / len(quiz_data)):.0%}" # show users score as a percentage
        )

        #place label at an suitable coordinate
        percentage_label.place(relx=0.54, rely=0.675, anchor="center", width=120, height=80)

        # or label
        or_label = tk.Label(  # create percentage label using tkinter
            result_window,  # place in result_window
            font=("Fredoka", 20, "bold"),  # font, font size, make bold
            bg="white",  # set background to white
            activebackground="#182156",  # set active background to dark blue
            highlightthickness=0,  # remove highlight thickness
            relief="flat",  # #removes all 3D borders and shadowing from label
            text="or"  #text
        )

        # place label at an suitable coordinate
        or_label.place(relx=0.445, rely=0.675, anchor="center", width=115, height=80)

        #congratulating user based on whether they have passed or failed
        if score >= 9:  #if score is equal or greater than 9
            end_text = f"Cheers to you for a job well done, {username}!"    #text to user
        else:   #else
            end_text = f"Good effort {username}!"   #text to user

        #greet user
        end_label = tk.Label(   #create and name label
            result_window,  #put in end window
            bg="white", #make background white
            text= end_text, #show positive or negative text based on users score
            font = ("Fredoka", 15, "bold"), #change font to Fredoka, make font size 15, and make bold
        )

        # place label at an suitable coordinate
        end_label.place(x=350, y=230, width=400, height=59)

        #def function for quit button
        def quit_quiz():  # create def function
            global warning_is_open  # use global variable to be able to use warning_is_open which filter controls whether warnings are ignored, displayed, or turned into errors.

            # If a warning is already on screen, exit immediately
            if warning_is_open:
                return  # return back

            # Set lock to True before showing the following message box
            warning_is_open = True
            answer = messagebox.askyesno(  # create confirmation messagebox
                "Exit Quiz Confirmation",  # title
                "Are you sure you want to quit?\n\n"  # text
                "If so, feel free to come back anytime!",  # text
                parent=result_window)  # pin messagebox on top of my main game window

            if answer:  # if yes
                root.destroy()  # end code by destroying window

            # Reset lock to False only after the user closes/exits the message box
            warning_is_open = False

        #exit button
        exit_button = tk.Button(    #create and name button
            result_window,  #put in end window
            font=("Fredoka", 30, "bold"),  # font and size of the text and make text bold
            fg="black",  # set text colour to back
            text="EXIT", #text
            bg="white",  # set label background colour to white
            relief="flat",  # removes all 3D borders and shadowing from button
            cursor="hand2",  # change cursor to hand to let users know this button is clickable
            command = quit_quiz #run command with following def function
        )

        #place button at an suitable coordinate
        exit_button.place(x=587, y=540, width=130, height=75)

        def play_again():
            global score    #to be able to track score
            global current_index    #to be able to track progress
            global selected_choice #to be able to reset selected choice when clicking on button
            score = 0   #reset score
            current_index = 0   #reset index
            selected_choice = None  #reset selected choice

            random.shuffle(quiz_data)   #reshuffle questions in dictionary

            new_window.destroy()    #destroy questions window

            result_window.destroy() #destroy end window

            open_next_window()  #head back to questions page

        #play again button
        play_again_button = tk.Button(  #create and name button using tkinter
            result_window,  #place in end window
            text="PLAY AGAIN",  #text
            wraplength=100,  # automatically break the text into a new line if it exceeds 100 pixels in width
            font=("Fredoka", 23, "bold"),   #change font to Fredoka, make font size 23, make bold
            fg="black", #set font colour to black
            bg="white", # set label background colour to white
            relief="flat", # removes all 3D borders and shadowing from button
            cursor="hand2", #change cursor to hand to let users know this button is clickable
            command=play_again  #head to the play again function
        )

        #place button at an suitable coordinate
        play_again_button.place(x=370, y=540, width=130, height=75)

        #applying same hover effects to buttons to be consistent with other buttons and to further help users
        def on_enter(event):    #hovering over a button
            event.widget.config(bg="#D6D6D6")   #change colour of button to gray

        def on_leave(event):    #stop hovering over a button
            event.widget.config(bg="white") #change colour back to white

        play_again_button.bind("<Enter>", on_enter) #bind to play_again button
        play_again_button.bind("<Leave>", on_leave) #bind to play_again button

        exit_button.bind("<Enter>", on_enter) #bind to exit button
        exit_button.bind("<Leave>", on_leave) #bind to exit button

    root.withdraw() #hide the start window

root.mainloop() #run the loop to keep window open