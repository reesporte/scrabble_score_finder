import sys
from tkinter import *
from scoring import score

DEBUG = False

def main():
    top = Tk()

    top.title("Scrabble Score")

    entry = Entry(top, bd = 5)
    entry.pack()

    var = StringVar()
    message = Message(top, textvariable=var)
    button = Button(top, text = "score", command = lambda: var.set(score(entry.get())))

    message.pack()
    button.pack()
    top.mainloop()

if __name__ == '__main__':
    main()
