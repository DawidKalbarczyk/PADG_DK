from tkinter import *


def newWindow(type, parentWindow):
    window = Toplevel(parentWindow)
    window.iconbitmap('assets/icons/form-18.ico')
    window.title("Formularz")
    window.geometry("600x400")
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    windowFrame = Frame(window)
    windowFrame.grid(row=0, column=0, sticky="nsew", columnspan=3)
    windowFrame.columnconfigure(0, weight=1)
    windowFrame.columnconfigure(1, weight=1)
    windowFrame.columnconfigure(2, weight=1)
    windowFrame.rowconfigure(0, weight=1)
    windowFrame.rowconfigure(1, weight=1)


    match type:
        case "add":
            windowText = Label(windowFrame, text = "Wpisz dane nowego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")
        case "edit":
            windowText = Label(windowFrame, text = "Wpisz nowe dane dla wybranego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")


