import tkinter as tk

from library.additionalFiles.windowPosition import windowPos
from library.engine import dbConnect
def newWindow(type, parentWindow, table):
    window = tk.Toplevel(parentWindow)
    window.iconbitmap('assets/icons/form-18.ico')
    window.title("Formularz")
    windowPos(root=window, windowWidth=600, windowHeight=400)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    windowFrame = tk.Frame(window)
    windowFrame.grid(row=0, column=0, sticky="nsew", columnspan=3)
    windowFrame.columnconfigure(0, weight=1)
    windowFrame.columnconfigure(1, weight=1)
    windowFrame.columnconfigure(2, weight=1)
    windowFrame.rowconfigure(0, weight=1)
    windowFrame.rowconfigure(1, weight=1)




    match type:
        case "add":
            windowText = tk.Label(windowFrame, text = "Wpisz dane nowego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")
            columnNames = generateEntryFromSQL(table)
            for idx, columnName in enumerate(columnNames):
                windowGeneratedSQL = Frame(windowFrame)
                windowGeneratedSQL

        case "edit":
            windowText = tk.Label(windowFrame, text = "Wpisz nowe dane dla wybranego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")

def generateEntryFromSQL(table):
    cursor = dbConnect().cursor()
    SQL = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cursor.execute(SQL)
    columns = cursor.fetchall()
    print(columns)
    columnNames = []
    for tuples in columns:
        for columnName in tuples:
            columnNames.append(columnName)
    return columnNames

