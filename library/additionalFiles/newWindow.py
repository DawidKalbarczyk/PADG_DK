import tkinter as tk


from library.additionalFiles.windowPosition import windowPos
from library.engine import dbConnect
def newWindow(type, parentWindow, selectedTableValue, listboxLine=None):
    window = tk.Toplevel(parentWindow)
    window.withdraw()
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

    selectedTableKey = ""
    from tkinter import messagebox
    match selectedTableValue:
        case "sklepy":
            selectedTableKey = "stores"
            window.deiconify()
        case "pracownicy":
            selectedTableKey = "employeesInStore"
            window.deiconify()
        case "dostawcy":
            selectedTableKey = "deliveryMen"
            window.deiconify()
        case "dostawy":
            selectedTableKey = "deliveries"
            window.deiconify()
        case "pracownicy-w-sklepie":
            messagebox.showerror("Błąd", "W celu dodania rekordu, należy wybrać jedną z tabel: Sklepy, Pracownicy, Dostawcy, Dostawy")
            window.destroy()
            return
        case "dostawcy-w-sklepie":
            messagebox.showerror("Błąd", "W celu dodania rekordu, należy wybrać jedną z tabel: Sklepy, Pracownicy, Dostawcy, Dostawy")
            window.destroy()
            return
    print(selectedTableKey)

    generatedStructure = []
    columnNamesString = ""
    match type:
        case "add":
            windowText = tk.Label(windowFrame, text = "Wpisz dane nowego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")
            windowGeneratedSQL = tk.Frame(windowFrame)
            windowGeneratedSQL.grid(row=1, column=0, sticky="nsew", columnspan=3, pady=20, padx=(0,40))
            windowGeneratedSQL.columnconfigure(0, weight=1)
            windowGeneratedSQL.columnconfigure(1, weight=3)
            struct, columnNames = generateEntryFromSQL(root=windowGeneratedSQL, table=selectedTableKey, struct=generatedStructure)
            columNamesString = ""
            for columnName in columnNames:
                columnNamesString += '"' + columnName + '", '
            columnNamesString = columnNamesString[:-2]
            windowAddButton = tk.Button(windowFrame, text = "Dodaj uzytkownika", command = lambda: addUser(window, struct, selectedTableKey, columnNamesString))
            windowAddButton.grid(row=2, column=1, sticky="ew")

        case "edit":
            windowText = tk.Label(windowFrame, text = "Wpisz nowe dane dla wybranego rekordu", font=("Roboto", 12))
            windowText.grid(row=0, column=1, sticky="ew")
            windowGeneratedSQL = tk.Frame(windowFrame)
            windowGeneratedSQL.grid(row=1, column=0, sticky="nsew", columnspan=3, pady=20, padx=(0,40))
            windowGeneratedSQL.columnconfigure(0, weight=1)
            windowGeneratedSQL.columnconfigure(1, weight=3)
            struct, columnNames = generateEntryFromSQL(root=windowGeneratedSQL, table=selectedTableKey,
                                                       struct=generatedStructure)
            columnNames.pop(-1)
            sqlIndex = listboxLine.split()[0]
            from library.additionalFiles.translationDict import DictReverse
            for i,name in enumerate(columnNames):
                columnNames[i] = DictReverse.get(columnNames[i], columnNames[i])

            print(columnNamesString)
            conn = dbConnect()
            cursor = conn.cursor()
            #SQL = f'UPDATE {selectedTableValue} SET'

            windowEditButton = tk.Button(windowFrame, text="Edytuj użytkownika",
                                        command=lambda: editUser(window, struct, selectedTableKey, columnNames, sqlIndex))
            windowEditButton.grid(row=2, column=1, sticky="ew")

def editUser(root, struct, table, columnNames, sqlIndex):
    infoToSQL = []
    for label, entry in struct:
        info = entry.get()
        infoToSQL.append(info)

    finalString = ""
    for column, value in zip(columnNames,infoToSQL):
        finalString += f'"{column}" = \'{value}\','
    finalString = finalString[:-1]
    print(finalString)
    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f'UPDATE public."{table}" SET {finalString} WHERE id = {sqlIndex};'
    print(SQL)
    cursor.execute(SQL)
    conn.commit()
    conn.close()
    root.destroy()

    # windowAddButton = tk.Button(windowFrame, text="Dodaj uzytkownika",
            #                             command=lambda: addUser(window, struct, selectedTableKey, columnNamesString))
            # windowAddButton.grid(row=2, column=1, sticky="ew")

def generateEntryFromSQL(root,table, struct):
    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
    cursor.execute(SQL)
    columns = cursor.fetchall()
    columnNames = []
    from library.additionalFiles.translationDict import Dict
    for tuples in columns:
        for columnName in tuples:
            displayName = Dict.get(columnName, columnName.upper())
            columnNames.append(displayName)
    columnNames.pop(0)
    columnNames.pop(-1)
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
