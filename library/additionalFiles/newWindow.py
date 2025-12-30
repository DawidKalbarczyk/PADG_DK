import tkinter as tk


from library.additionalFiles.windowPosition import windowPos
from library.engine import dbConnect
from tkinter import messagebox
def newWindow(type, parentWindow, selectedTableValue, objectsList=None, pickFrame=None):
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
    showDatabaseType = "single"
    store = None
    if type == "add":
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
                selectedTableKey = "employeesInStore"
                window.deiconify()
                showDatabaseType = "multi"
                if objectsList.size() > 1:
                    store = objectsList.get(1).split()[-1]
                else:
                    messagebox.showinfo("Informacja", "Brak rekordów do pokazania. Dodaj rekord w podstawowej tabeli.")


            case "dostawcy-w-sklepie":
                selectedTableKey = "deliveryMen"
                window.deiconify()
                showDatabaseType = "multi"
                if objectsList.size() > 1:
                    store = objectsList.get(1).split()[-1]
                else:
                    messagebox.showinfo("Informacja", "Brak rekordów do pokazania. Dodaj rekord w podstawowej tabeli.")




    elif type == "edit" and objectsList.curselection():
        window.deiconify()

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
                response = messagebox.askyesno("Informacja","Edytujesz rekord z tabeli pracowników. \nCzy na pewno chcesz kontynuować?")
                if response:
                    selectedTableKey = "employeesInStore"
                    window.deiconify()
                    showDatabaseType = "multi"
                    store = objectsList.get(objectsList.curselection()).split()[-1]
                else:
                    window.destroy()
                    return


            case "dostawcy-w-sklepie":
                response = messagebox.askyesno("Informacja","Edytujesz rekord z tabeli pracowników. \nCzy na pewno chcesz kontynuować?")
                if response:
                    selectedTableKey = "deliveryMen"
                    window.deiconify()
                    showDatabaseType = "multi"
                    store = objectsList.get(objectsList.curselection()).split()[-1]
                else:
                    window.destroy()
                    return


    elif type == "delete" and objectsList.curselection():
        match selectedTableValue:
            case "sklepy":
                selectedTableKey = "stores"

            case "pracownicy":
                selectedTableKey = "employeesInStore"

            case "dostawcy":
                selectedTableKey = "deliveryMen"

            case "dostawy":
                selectedTableKey = "deliveries"

            case "pracownicy-w-sklepie":
                selectedTableKey = "employeesInStore"
                showDatabaseType = "multi"
                store = objectsList.get(objectsList.curselection()).split()[-1]

            case "dostawcy-w-sklepie":
                selectedTableKey = "deliveryMen"
                showDatabaseType = "multi"
                store = objectsList.get(objectsList.curselection()).split()[-1]

    else:
        messagebox.showerror("Błąd", "Żaden rekord nie jest zaznaczony.")
        return


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
            columnNamesString = ""
            for columnName in columnNames:
                columnNamesString += '"' + columnName + '", '
            columnNamesString = columnNamesString[:-2]
            from library.additionalFiles.showDatabase import showDatabase

            windowAddButton = tk.Button(windowFrame, text = "Dodaj uzytkownika", command = lambda: [
                addUser(window, struct, selectedTableKey, columnNamesString),
                showDatabase(objectsList, showDatabaseType, selectedTableKey, store=store, pickFrame=pickFrame)
            ])
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
            sqlIndex = objectsList.get(objectsList.curselection()).split()[0]
            from library.additionalFiles.translationDict import DictReverse
            for i,name in enumerate(columnNames):
                columnNames[i] = DictReverse.get(columnNames[i], columnNames[i])

            from library.additionalFiles.showDatabase import showDatabase
            windowEditButton = tk.Button(windowFrame, text="Edytuj użytkownika", command=lambda: [
                editUser(window, struct, selectedTableKey, columnNames, sqlIndex),
                showDatabase(objectsList, showDatabaseType, selectedTableKey, store=store, pickFrame=pickFrame)
            ])
            windowEditButton.grid(row=2, column=1, sticky="ew")
        #TODO Dodać, że jeżeli podświetlony przycisk lewy dolny lub prawy dolny to po add, edit itd aktualizacja za pomocą showDatabase
        #TODO - teoretycznie po dodaniu,edit, i delete powinno się odświeżać ale nwm o co chodzi
        case "delete":
            sqlIndex = objectsList.get(objectsList.curselection()).split()[0]
            SQL = f'DELETE FROM public."{selectedTableKey}" WHERE id = {sqlIndex}'
            response = messagebox.askyesno("Informacja", f"Czy jesteś pewien, że chcesz usunąć rekord o ID:"
                                                       f" {sqlIndex}? Zmiany są nieodwracalne.")
            from library.additionalFiles.showDatabase import showDatabase
            if response:
                conn = dbConnect()
                cursor = conn.cursor()
                cursor.execute(SQL)
                conn.commit()
                conn.close()
                showDatabase(objectsList, showDatabaseType, selectedTableKey, store=store, pickFrame=pickFrame)
            else:
                window.destroy()
                return
            messagebox.showinfo("Informacja", f"Usunięto rekord o ID: {sqlIndex}")
def editUser(root, struct, table, columnNames, sqlIndex):
    infoToSQL = []
    for label, entry in struct:
        info = entry.get()
        infoToSQL.append(info)

    finalString = ""
    for column, value in zip(columnNames,infoToSQL):
        finalString += f'"{column}" = \'{value}\','
    finalString = finalString[:-1]

    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f'UPDATE public."{table}" SET {finalString} WHERE id = {sqlIndex};'

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
    if table == "employeesInStore":
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

    columnNamesList = columnNamesString.replace('"', '').split(', ')
    reversedColumnNames = []
    from library.additionalFiles.translationDict import DictReverse
    for columnName in columnNamesList:
        reversedName = DictReverse.get(columnName, columnName)
        reversedColumnNames.append(f'"{reversedName}"')

    reversedColumnNamesString = ', '.join(reversedColumnNames)
    conn = dbConnect()
    cursor = conn.cursor()
    SQL = f'INSERT INTO public."{table}"({reversedColumnNamesString}) VALUES ({infoToSQLString})'
    cursor.execute(SQL)
    conn.commit()
    conn.close()
    root.destroy()
