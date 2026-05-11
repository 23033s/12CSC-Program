import tkinter as tk #import the main GUI library to my program
from PIL import Image, ImageTk #import Pillow to handle images
import pyglet #import pyglet to use custom font
from tkinter import messagebox
quiz_data = {
    "Easy": [
        {"question": "What planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What gas do humans need to breathe?", "choices": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
        {"question": "Which organ pumps blood in the human body?", "choices": ["Brain", "Lungs", "Heart", "Kidney"], "answer": "Heart"},
        {"question": "Which state of matter has a fixed shape?", "choices": ["Liquid", "Gas", "Solid", "Plasma"], "answer": "Solid"},
        {"question": "What is the freezing point of water?", "choices": ["0°C", "50°C", "100°C", "-10°C"], "answer": "0°C"}
    ],
    "Medium": [
        {"question": "Which blood cell carries oxygen?", "choices": ["White blood cells", "Red blood cells", "Platelets", "Plasma"], "answer": "Red blood cells"},
        {"question": "Which energy transformation occurs in a moving car?", "choices": ["Chemical → kinetic", "Kinetic → chemical", "Thermal → light", "Light → sound"], "answer": "Chemical → kinetic"},
        {"question": "Which planet has the strongest gravity?", "choices": ["Saturn", "Earth", "Venus", "Jupiter"], "answer": "Jupiter"},
        {"question": "What is friction mainly caused by?", "choices": ["Gravity", "Surface contact", "Magnetism", "Light"], "answer": "Surface contact"},
        {"question": "Which part of the cell controls activities?", "choices": ["Cytoplasm", "Nucleus", "Membrane", "Ribosome"], "answer": "Nucleus"}
    ],
    "Hard": [
        {"question": "What is the chemical symbol for potassium?", "choices": ["P", "K", "Pt", "Po"], "answer": "K"},
        {"question": "What type of bond involves sharing electrons?", "choices": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "answer": "Covalent"},
        {"question": "Which part of the brain controls voluntary actions?", "choices": ["Cerebellum", "Cerebrum", "Brainstem", "Neuron"], "answer": "Cerebrum"},
        {"question": "Which gas is most abundant in Earth’s atmosphere?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen"},
        {"question": "What is the pH of a neutral solution?", "choices": ["0", "7", "14", "10"], "answer": "7"}
    ],
    "Challenging": [
        {"question": "In the Heisenberg uncertainty principle, which two properties cannot be observed precisely at the same time?", "choices": ["Velocity and Acceleration", "Mass and Energy", "Position and Momentum", "Spin and Charge"], "answer": "Position and Momentum"},
        {"question": "What is the main purpose of enzymes?", "choices": ["Store energy", "Speed up reactions", "Carry oxygen", "Break bones"], "answer": "Speed up reactions"},
        {"question": "What is the name of the radiation emitted by black holes due to quantum effects?", "choices": ["Synchrotron radiation", "Hawking radiation", "Cherenkov radiation", "Bremsstrahlung"], "answer": "Hawking radiation"},
        {"question": "Which of the following is the SI unit of luminous intensity?", "choices": ["Lumen", "Lux", "Candela", "Watt"], "answer": "Candela"},
        {"question": "Which type of quark is the heaviest?", "choices": ["Up", "Bottom", "Top", "Charm"], "answer": "Top"}
    ],
    "Mix": [
        {"question": "What is the rarest naturally occurring element on Earth?", "choices": ["Uranium", "Astatine", "Francium", "Rhodium"], "answer": "Astatine"},
        {"question": "Which protein is primarily responsible for the maintenance of osmotic pressure in blood?", "choices": ["Gamma globulin", "Immunoglobulin", "Beta macroglobulin", "Albumin"], "answer": "Albumin"},
        {"question": "What is the chemical symbol for gold?", "choices": ["Au", "Ag", "Gd", "Go"], "answer": "Au"},
        {"question": "What is the powerhouse of the cell?", "choices": ["Nucleus", "Mitochondria", "Ribosome", "Membrane"], "answer": "Mitochondria"},
        {"question": "What is the chemical formula for water?", "choices": ["CO2", "H2O", "O2", "NaCl"], "answer": "H2O"}
    ],
    "TrueFalse": [
        {"question": "The Moon is bigger than Earth.", "choices": ["True", "False"], "answer": "False"},
        {"question": "Plants absorb oxygen during photosynthesis.", "choices": ["True", "False"], "answer": "False"},
        {"question": "A photon has zero mass and cannot exert physical pressure.", "choices": ["True", "False"], "answer": "False"},
        {"question": "Electricity is a form of energy.", "choices": ["True", "False"], "answer": "True"},
        {"question": "Momentum depends on both mass and velocity.", "choices": ["True", "False"], "answer": "True"}
    ]
}
pyglet.font.add_file("fonts/Fredoka.ttf") #Load the font file from folder
root = tk.Tk() #create intro window
root.geometry("1225x690") #resize window
root.resizable(False, False)
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

outcome_label = tk.Label(root, text="Please Enter In Your Name", font=("Arial", 15)) #Ask user to enter their name
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
    new_window.geometry("1225x690")
    new_window.resizable(False, False)
    next_img = Image.open("Images/q1.png") #open background image for first question
    next_photo = ImageTk.PhotoImage(next_img) #convert image to a format tkinter can use
    img_label = tk.Label(new_window, image=next_photo) #create a label widget to display background image
    img_label.image = next_photo #reference image
    img_label.pack(pady=10) #add padding to main window
    answer_buttons = []

    button_positions = [

        (0.28, 0.58),
        (0.66, 0.58),
        (0.28, 0.82),
        (0.66, 0.82)
    ]
    submit_button = tk.Button(
        new_window,
        text="Submit",
        font="Fredoka",
        size="30",
        bg="white",
        relief="flat")
    submit_button.place(relx=0.78, rely=0.42, anchor="center")
    root.withdraw() #hide the window

root.mainloop() #run the loop to keep window open
