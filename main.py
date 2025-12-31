import tkinter as tk
from library.engine import dbConnect
from library.gui import graphicUserInterface
from library.loginInterface import login

def main():
    root = tk.Tk()
    isLogged = login(root)
    if isLogged == True:
        graphicUserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
