from tkinter import *
from constants import *
import csv


# Windows
def makeWindow(x=windowWidth, y=windowHeight):
    root = Tk()
    root.pages = {}
    root.data = {
        "app": {
            "question": 0,
            "questionText": None,
            "questionNumber": None,
            "nextButton": None,
            "radioButtons": []
        }
    }

    setTitle(root, "Illness Consultant Program")
    setSize(root, x, y)
    setNotResizable(root)

    return root

def setTitle(root, name):
    root.title(name);

def setSize(root, width, height):
    x = int(root.winfo_screenwidth() / 2 - width / 2)
    y = int(root.winfo_screenheight() / 2 - height / 2)

    root.geometry("{}x{}+{}+{}".format(width, height, x, y))

def setNotResizable(root):
    root.resizable(0, 0)


# Pages
def destroyPage(root, page):
    if not page in root.pages:
        return False

    for _, component in root.pages[page].items():
        component.destroy()

    root.pages[page] = {}
