from library.engine import dbConnect
from library.additionalFiles.guiFunctions import removeCursorSelection
def showDatabase(rootListbox, type, table="employeesInStore", table2=None, pickFrame=None):
    match type:
        case "single":
            rootListbox.delete(0, "end")
            conn = dbConnect()
            cursor = conn.cursor()
            SQLcolumns = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'"
            cursor.execute(SQLcolumns)
            columns = cursor.fetchall()
            SQLdata = ""


            match table:
                case "stores":
                    columns.pop(1)
                    columns.pop(3)
                    SQLdata = f'SELECT id,owner,"employeesNr" FROM "{table}" ORDER BY id ASC'
                case "employeesInStore":
                    columns.pop(1)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(4)
                    SQLdata = f'SELECT id,"firstName","lastName",store FROM "{table}" ORDER BY id ASC'
                case "deliveryMen":
                    columns.pop(1)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    SQLdata = f'SELECT id,"firstName","lastName",store FROM "{table}" ORDER BY id ASC'
                case "deliveries":
                    columns.pop(1)
                    columns.pop(1)
                    columns.pop(1)
                    SQLdata = f'SELECT id, date, distance FROM "{table}" ORDER BY id ASC'

            cursor.execute(SQLdata)
            dataDatabase = cursor.fetchall()
            columnNames = []
            dataColumns = []


            for tuples in columns:
                for columnName in tuples:
                    columnNames.append(columnName.upper())
            for data in dataDatabase:
                dataColumns.append(str(data))


            if len(columnNames)==3:
                col1,col2,col3 = columnNames[0].ljust(16), columnNames[1].ljust(16), columnNames[2].ljust(16)
                rootListbox.insert("end", f"{col1} {col2} {col3}")
                for data in dataColumns:
                    datTemp = []
                    data = data[1:-1]
                    data = data.split()
                    for dat in data:
                        dat = dat.strip(",")
                        dat = dat.strip("'")
                        datTemp.append(dat)
                    datTemp[0], datTemp[1], datTemp[2] = datTemp[0].ljust(16),datTemp[1].ljust(16),datTemp[2].ljust(16)
                    rootListbox.insert("end", f"{datTemp[0]} {datTemp[1]} {datTemp[2]}")



            elif len(columnNames)==4:
                col1, col2, col3, col4= columnNames[0].ljust(7), columnNames[1].ljust(12), columnNames[2].ljust(15), columnNames[3].ljust(7)
                rootListbox.insert("end", f"{col1} {col2} {col3} {col4}")
                for data in dataColumns:
                    datTemp = []
                    data = data[1:-1]
                    data = data.split()
                    for dat in data:
                        dat = dat.strip(",")
                        dat = dat.strip("'")
                        datTemp.append(dat)
                    datTemp[0], datTemp[1], datTemp[2], datTemp[3]= (
                        datTemp[0].ljust(7), datTemp[1].ljust(12),
                        datTemp[2].ljust(15), datTemp[3].ljust(7))

                    rootListbox.insert("end", f"{datTemp[0]} {datTemp[1]} {datTemp[2]} {datTemp[3]}")
            cursor.close()

        case "multi":
            import tkinter as tk
            objectsPickFrame = tk.Frame(pickFrame)
            #objectsPickFrame.bind_all("<Button-1>",lambda event: event.widget.focus_set())
            objectsPickFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=(20,0))
            objectsPickFrame.columnconfigure(0, weight=1)
            objectsPickFrame.columnconfigure(1, weight=1)
            objectsPickFrame.columnconfigure(2, weight=1)
            objectsPickFrame.rowconfigure(0, weight=1)
            objectsPickFrame.rowconfigure(1, weight=2)


            objectsPickTitle = tk.Label(objectsPickFrame, text="Wybierz sklep", font=("Roboto", 10, "bold"))
            objectsPickTitle.grid(row=0, column=1, sticky="nsew")


            def pickOptionLabels():
                title = ""
                if table == "employeesInStore":
                    title = "Pracownicy dla: "
                elif table == "deliveryMen":
                    title = "Dostawcy dla: "
                return title
            objectsPickOptionTitle = tk.Label(objectsPickFrame, text=f"{pickOptionLabels()}")
            objectsPickOptionTitle.grid(row=1, column=0, sticky="nsew")


            def pickOptionWindow(root, pickListbox):
                pickListbox.delete(0, tk.END)
                root.deiconify()
                cursor = dbConnect().cursor()
                SQL2 = 'SELECT id, address, owner FROM "stores" ORDER BY id ASC'
                cursor.execute(SQL2)
                dataDatabase = cursor.fetchall()
                dataColumns = []

                SQL1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'stores'"
                cursor.execute(SQL1)
                columns = cursor.fetchall()

                columnNames = []

                for tuples in columns:
                    for columnName in tuples:
                        columnNames.append(columnName.upper())

                columnNames.pop(3)
                columnNames.pop(3)
                col1, col2, col3 = columnNames[0].ljust(45), columnNames[1].ljust(45), columnNames[2].ljust(45)

                pickListbox.insert("end", f"{col1} {col2} {col3}")
                for data in dataDatabase:
                    dataColumns.append(str(data))
                    dat1, dat2, dat3 = str(data[0]).ljust(45), str(data[1]).ljust(45), str(data[2]).ljust(45)
                    pickListbox.insert("end", f"{dat1} {dat2} {dat3}")





                cursor.close()

            from library.additionalFiles.windowPosition import windowPos
            pickWindow = tk.Toplevel()
            pickWindow.withdraw()
            pickWindow.columnconfigure(0, weight=1)
            pickWindow.columnconfigure(1, weight=1)
            pickWindow.columnconfigure(2, weight=1)
            pickWindow.rowconfigure(0, weight=1)
            pickWindow.rowconfigure(1, weight=9)
            pickWindow.rowconfigure(2, weight=1)
            windowPos(root=pickWindow, windowWidth=900, windowHeight=500)
            pickWindow.title("Formularz wyboru")
            pickWindow.iconbitmap("assets/icons/form-18.ico")
            cursor = dbConnect().cursor()





            pickWindowTitle = tk.Label(pickWindow, text="Wybierz sklep", font=("Courier", 14, "bold"))
            pickWindowTitle.grid(row=0, column=1, sticky="nsew")

            pickWindowListbox = tk.Listbox(pickWindow)
            pickWindowListbox.grid(row=1, column=0, sticky="nsew", columnspan=3, pady=(10, 0))
            pickWindowListbox.config(font=("Courier", 8), activestyle='none')
            removeCursorSelection(pickWindowListbox)
            pickWindowListbox.delete(0, tk.END)

            def pickListboxElement():
                selectedElementNative = pickWindowListbox.curselection()
                selectedElement = pickWindowListbox.get(selectedElementNative[0])
                storeID = selectedElement.split()
                storeID = storeID[0].strip()
                return storeID

            #def

            pickWindowButton = tk.Button(pickWindow, text="Akceptuj", font=("Courier", 12), command=lambda: pickedOption(pickWindow, pickListboxElement()))
            pickWindowButton.grid(row=2, column=1, sticky="ew")


            objectsPickOptionButton = tk.Button(objectsPickFrame, text="Wybierz", command=lambda: pickOptionWindow(pickWindow, pickWindowListbox))
            objectsPickOptionButton.grid(row=1, column=1, sticky="nsew", padx=(7,10))


            objectsPickOptionEndTitle = tk.Label(objectsPickFrame, text="sklepu")
            objectsPickOptionEndTitle.grid(row=1, column=2, sticky="nsew")





            # TODO zrob generowanie w nowym okienku opcji do wyboru z przyciskiem "Ackeptuj"
            # TODO dodaj generowanie z sqla wierszy z wartosciami

            match table:
                case "employeesInStore":
                    def pickedOption(toDestroy, element):
                        rootListbox.delete(0, tk.END)
                        cursor = dbConnect().cursor()
                        SQLconditionData = f'SELECT id,"firstName","lastName",store FROM "employeesInStore" WHERE store=\'{element}\''
                        cursor.execute(SQLconditionData)
                        SQLdataBack = cursor.fetchall()

                        SQL1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'employeesInStore'"
                        cursor.execute(SQL1)
                        columns = cursor.fetchall()

                        columnNames = []

                        for tuples in columns:
                            for columnName in tuples:
                                columnNames.append(columnName.upper())
                        print(columnNames)
                        columnNames.pop(1)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        columnNames.pop(4)
                        col1, col2, col3, col4 = columnNames[0].ljust(7), columnNames[1].ljust(12), columnNames[2].ljust(15), columnNames[3].ljust(7)

                        rootListbox.insert("end", f"{col1} {col2} {col3} {col4}")

                        for data in SQLdataBack:
                            dat1, dat2, dat3, dat4 = (str(data[0]).ljust(7), str(data[1]).ljust(12),
                                                      str(data[2]).ljust(15), str(data[3]).ljust(7))
                            rootListbox.insert("end", f"{dat1} {dat2} {dat3} {dat4}")

                        toDestroy.withdraw()
                        cursor.close()

                case "deliveryMen":
                    def pickedOption(toDestroy, element):
                        rootListbox.delete(0, tk.END)
                        cursor = dbConnect().cursor()
                        SQLconditionData = f'SELECT id,"firstName","lastName",store FROM "deliveryMen" WHERE store=\'{element}\''
                        cursor.execute(SQLconditionData)
                        SQLdataBack = cursor.fetchall()

                        SQL1 = "SELECT column_name FROM information_schema.columns WHERE table_name = 'deliveryMen'"
                        cursor.execute(SQL1)
                        columns = cursor.fetchall()

                        columnNames = []

                        for tuples in columns:
                            for columnName in tuples:
                                columnNames.append(columnName.upper())
                        print(columnNames)
                        columnNames.pop(1)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        columnNames.pop(3)
                        col1, col2, col3, col4 = columnNames[0].ljust(7), columnNames[1].ljust(12), columnNames[2].ljust(15), columnNames[3].ljust(7)

                        rootListbox.insert("end", f"{col1} {col2} {col3} {col4}")
                        print(SQLdataBack)
                        for data in SQLdataBack:
                            dat1, dat2, dat3, dat4 = (str(data[0]).ljust(7), str(data[1]).ljust(12),
                                                      str(data[2]).ljust(15), str(data[3]).ljust(7))
                            rootListbox.insert("end", f"{dat1} {dat2} {dat3} {dat4}")

                        toDestroy.withdraw()
                        cursor.close()


            cursor.close()
    removeCursorSelection(rootListbox)

    #print(columnNames)
    #print(dataColumns)