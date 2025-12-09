import tkinter as tk


from library.additionalFiles.windowPosition import windowPos
from library.engine import dbConnect
def newWindow(type, parentWindow, table):
    window = tk.Toplevel(parentWindow)
    window.iconbitmap('assets/icons/form-18.ico')
    window.title("Formularz")
    windowPos(root=window, windowWidth=400, windowHeight=400)
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
    windowFrame.rowconfigure(2, weight=1)




    match type:
        case "add":
            windowText = tk.Label(windowFrame, text = "Wpisz dane nowego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")
            windowGeneratedSQL = tk.Frame(windowFrame)
            windowGeneratedSQL.grid(row=1, column=0, sticky="nsew", columnspan=3, pady=20, padx=(0,40))
            windowGeneratedSQL.columnconfigure(0, weight=1)
            windowGeneratedSQL.columnconfigure(1, weight=3)
            generatedStructure = []
            conn = dbConnect()
            cursor = conn.cursor()
            struct, columnNames = generateEntryFromSQL(root=windowGeneratedSQL, table=table, struct=generatedStructure)
            print(struct)
            print(columnNames)
            columnNamesString = ""
            for columnName in columnNames:
                columnNamesString += '"' + columnName + '", '
            columnNamesString = columnNamesString[:-2]
            print(columnNamesString)
            windowAddButton = tk.Button(windowFrame, text = "Dodaj uzytkownika", command = lambda: addUser(window, struct, table, columnNamesString))
            windowAddButton.grid(row=2, column=1, sticky="ew")






        case "edit":
            windowText = tk.Label(windowFrame, text = "Wpisz nowe dane dla wybranego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")

def generateEntryFromSQL(root,table, struct):
    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cursor.execute(SQL)
    columns = cursor.fetchall()
    columnNames = []
    for tuples in columns:
        for columnName in tuples:
            columnNames.append(columnName)
    columnNames.pop(0)
    for i in range(len(columnNames)-1):
        root.rowconfigure(i, weight=1)
    for idx, columnName in enumerate(columnNames):
        label = tk.Label(root, text=f"{columnName}: ", font=("Roboto", 12))
        label.grid(row=idx, column=0, sticky="ew")
        entry = tk.Entry(root)
        entry.grid(row=idx, column=1, sticky="ew")
        struct.append((label, entry))
    return struct, columnNames

def addUser(root, struct, table, columnNamesString):
    infoToSQL = []
    for label, entry in struct:
        info = entry.get()
        infoToSQL.append(info)
    infoToSQLString = ''
    for info in infoToSQL:
        infoToSQLString += "'" + info + "', "
    infoToSQLString = infoToSQLString[:-2]
    print(infoToSQLString)
    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f'INSERT INTO public."{table}"({columnNamesString}) VALUES ({infoToSQLString})'
    cursor.execute(SQL)
    conn.commit()
    conn.close()
    root.destroy()
