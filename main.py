from tkinter import *
from tkinter import messagebox
from utils import *
from constants import *


root = makeWindow()

# Array of questions that are later indexed by the program
questions = [
    "Do you have any sudden lumps?",
    "Do you have any small spots that may have become blisters/scabs?",
    "Do you have a runny nose or a sore throat?",
    "Do you have a loss of smell or taste?",
    "Do you have an aching body or vomiting?",
    "Do you have problems swallowing?"
]

def askQuestion(root, question): # question parameter = the question index
    # Destroy all compnenets of the older page, validation check because if its the first page they wont be valid
    if root.data["app"]["questionNumber"]:
        root.data["app"]["questionNumber"].destroy()

    if root.data["app"]["questionText"]:
        root.data["app"]["questionText"].destroy()

    for radio in root.data["app"]["radioButtons"]:
        radio.destroy();

    if root.data["app"]["nextButton"]:
        root.data["app"]["nextButton"].destroy()


    # User input choices
    choices = [ "Yes", "No" ]
    userSelection = IntVar();
    y = 0
    for index in range(len(choices)):
        radiobutton = Radiobutton(root, text=choices[index], variable=userSelection, value=index, padx=25, compound = 'left', font=("Century Gothic", 20))
        radiobutton.place(relx=0.44, rely=0.60 + y, anchor='w')
        y += 0.06

        root.data["app"]["radioButtons"].append(radiobutton);


            
    # Question Number
    questionNumber = Label(root, text="Question {}".format(question + 1), font=("Century Gothic", 20))
    questionNumber.place(relx=0.5, rely=0.10, anchor='center')


    # Question Text
    questionText = Label(root, text=question in range(0, len(questions)) and questions[question] or "unknown", font=("Century Gothic", 20))
    questionText.place(relx=0.5, rely=0.30, anchor='center')


    # Next Button
    nextButton = Button(root, text="Submit", font=("Century Gothic", 14), width=10, borderwidth=1, relief="solid", command=lambda: next(root, choices[userSelection.get()], question in range(0, len(questions)) and questions[question] or "unknown"))
    nextButton.place(relx=0.5, rely=0.81, anchor="center")


    # Assign components
    root.data["app"]["questionNumber"] = questionNumber
    root.data["app"]["questionText"] = questionText
    root.data["app"]["nextButton"] = nextButton



# Function to load the next question/register the users answer
def next(root, answer, question):
    question = root.data["app"]["question"]

    # If the user said they have a symptom
    if answer.lower() == "yes":
        # Get the illness from the question index
        illness = getIllness(question)
        messagebox.showerror(title="Attention!", message="You may have {}".format(illness));
        
        # Reset the question to the start
        root.data["app"]["question"] = 0;
        # Load that question
        askQuestion(root, root.data["app"]["question"]);
    else:
        # If the question is bigger or equal to the length of the questions - 1 (the end)
        if question >= len(questions) - 1:
            messagebox.showinfo(title="Attention!", message="You have reached the end");
            # Reset the question back to the start
            root.data["app"]["question"] = 0;
        else:
            # Adds one onto the question
            root.data["app"]["question"] += 1
        # Load the question
        askQuestion(root, question = root.data["app"]["question"])

# Get the illness from the question index
def getIllness(question):
    illness = None
    if question == 0:
        illness = "cancer";
    elif question == 1:
        illness = "chicken pox";
    elif question == 2:
        illness = "a cold";
    elif question == 3:
        illness = "COVID19";
    elif question == 4:
        illness = "the flu";
    elif question == 5:
        illness = "tonsillitis";

    return illness;

# Start the program by asking the first question
askQuestion(root, 0)

root.mainloop()
