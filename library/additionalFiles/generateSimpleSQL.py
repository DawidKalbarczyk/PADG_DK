import tkinter as tk


from library.additionalFiles.windowPosition import windowPos
def generateDetailsSQL(root, table):
    window = tk.Toplevel(root)
    window.title("Szczegóły")
    window.iconbitmap("assets/icons/more-info-icon.ico")
    windowPos(root=window, windowWidth=900, windowHeight=500)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.grid()
    windowFrame = tk.Frame(window)
    windowFrame.columnconfigure(0, weight=1)
    windowFrame.columnconfigure(1, weight=0)
    windowFrame.rowconfigure(0, weight=1)
    windowFrame.rowconfigure(1, weight=0)
    windowFrame.rowconfigure(2, weight=0)
    windowFrame.grid(row=0, column=0, sticky="nsew")
    root.protocol("WM_DELETE_WINDOW", lambda: window.destroy())

    windowListbox = tk.Listbox(windowFrame)
    windowListbox.grid(row=0, column=0, sticky="nsew")
    windowListbox.config(font=("Courier", 10), activestyle='none')

    windowListboxScrollbarY = tk.Scrollbar(windowFrame, orient="vertical", command=windowListbox.yview)
    windowListboxScrollbarY.grid(row=0, column=1, sticky="ns")
    windowListbox.config(yscrollcommand=windowListboxScrollbarY.set)

    windowListboxScrollbarX = tk.Scrollbar(windowFrame, orient="horizontal", command=windowListbox.xview)
    windowListboxScrollbarX.grid(row=1, column=0, sticky="ew")
    windowListbox.config(xscrollcommand=windowListboxScrollbarX.set)

    from library.engine import dbConnect
    conn = dbConnect()
    cursor = conn.cursor()
    SQLColumns = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}';"
    cursor.execute(SQLColumns)
    columns = cursor.fetchall()
    columns.pop(-1)
    columnNamesString = ""


    from library.additionalFiles.translationDict import Dict
    for tuples in columns:
        for columnName in tuples:
            displayName = Dict.get(columnName, columnName.upper())
            columnNamesString += displayName.ljust(27) + "|"
    windowListbox.insert("end", f"{columnNamesString}")

    separator = ""
    for _ in columnNamesString:
        separator += "-"

    windowListbox.insert("end", f"{separator}")

    SQLData = f'SELECT * FROM "{table}";'
    cursor.execute(SQLData)
    dataSQL = cursor.fetchall()
    dataSQL.pop(-1)

    separatorIDs = [0,1]
    for data in dataSQL:
        dataString = ""
        dataWithoutPass = []
        for d in data:
            dataWithoutPass.append(d)
        dataWithoutPass.pop(-1)
        for d in dataWithoutPass:
            d = str(d)
            dataString += d.ljust(27) + "|"
        windowListbox.insert("end", f"{dataString}")
        separator = ""
        for _ in dataString:
            separator += "-"
            separatorIDs.append(windowListbox.size())

        windowListbox.insert("end", f"{separator}")
        #dat1, dat2, dat3, dat4 = (str(data[0]).ljust(7), str(data[1]).ljust(12),
         #                         str(data[2]).ljust(15), str(data[3]).ljust(7))

    def deselectSeparators(uselessEvent):
        tempSelection = windowListbox.curselection()
        for idx in tempSelection:
            if idx in separatorIDs or idx == 1 or idx == 0:
                windowListbox.after(1, lambda index = idx: windowListbox.selection_clear(index))  ##
    windowListbox.bind("<<ListboxSelect>>", deselectSeparators)
    conn.close()
# TODO dodać generowanie szczegółów dla dwóch multi tablic
# TODO dodać do bazy dla deliveries data zamówienia i data dostarczenia