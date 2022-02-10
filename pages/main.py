from tkinter import *
from tkinter import messagebox
from utils import *


def main(root):
    askQuestion(root, root.data["app"]["question"])

def askQuestion(root, question):
    if root.data["app"]["questionNumber"]:
        print("destroy")
        root.data["app"]["questionNumber"].destroy()

    if root.data["app"]["nextButton"]:
        root.data["app"]["nextButton"].destroy()


    print("index {} = {}".format(question, question + 1))

    # Question Number
    questionNumber = Label(root, text="Question {}".format(question + 1), font=(None, 16))
    questionNumber.place(relx=0.5, rely=0.10, anchor='center')

    # Next Button
    nextButton = Button(root, text="Submit", font=(None, 17), width=10, borderwidth=1, relief="solid", command=lambda: next(root))
    nextButton.place(relx=0.5, rely=0.7, anchor="center")

    # Assign
    root.data["app"]["questionNumber"] = questionNumber
    root.data["app"]["nextButton"] = nextButton

def next(root):
    root.data["app"]["question"] += 1

    askQuestion(root, question = root.data["app"]["question"])