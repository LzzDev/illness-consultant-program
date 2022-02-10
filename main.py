from tkinter import *
from utils import *
from constants import *

from pages.main import *


root = makeWindow()

questions = [
    "Do you have any sudden lumps?",
    "Do you have any small spots that may have become blisters/scabs?",
    "Do you have a runny nose or a sore throat?",
    "Do you have a loss of smell or taste?",
    "Do you have an aching body or vomiting?",
    "Do you have problems swallowing?"
]

def askQuestion(root, question):
    if root.data["app"]["questionNumber"]:
        root.data["app"]["questionNumber"].destroy()

    if root.data["app"]["questionText"]:
        root.data["app"]["questionText"].destroy()

    for radio in root.data["app"]["radioButtons"]:
        radio.destroy();

    if root.data["app"]["nextButton"]:
        root.data["app"]["nextButton"].destroy()


    choices = [ "Yes", "No" ]

    x = IntVar();
    y = 0
    for index in range(len(choices)):
        radiobutton = Radiobutton(root, text=choices[index], variable=x, value=index, padx=25, compound = 'left', font=("Century Gothic", 20))
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
    nextButton = Button(root, text="Submit", font=("Century Gothic", 14), width=10, borderwidth=1, relief="solid", command=lambda: next(root, choices[x.get()], question in range(0, len(questions)) and questions[question] or "unknown"))
    nextButton.place(relx=0.5, rely=0.81, anchor="center")


    # Assign components
    root.data["app"]["questionNumber"] = questionNumber
    root.data["app"]["questionText"] = questionText
    root.data["app"]["nextButton"] = nextButton



def next(root, answer, question):
    if answer.lower() == "yes":
        question = root.data["app"]["question"]
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


        messagebox.showerror(title="Attention!", message="You may have {}".format(illness));
        root.data["app"]["question"] = 0;
        askQuestion(root, root.data["app"]["question"]);
    else:
        if root.data["app"]["question"] >= len(questions) - 1:
            messagebox.showinfo(title="Attention!", message="You have reached the end");
            root.data["app"]["question"] = 0;
        else:
            root.data["app"]["question"] += 1
        askQuestion(root, question = root.data["app"]["question"])

askQuestion(root, 0)

root.mainloop()
