from ..engine import dbConnect
def showDatabase(listbox, type, table="employeesInStore", table2=None, pickFrame=None):
    match type:
        case "single":
            listbox.delete(0, "end")
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
                    SQLdata = f'SELECT id,owner,"employeesNr" FROM {table}'
                case "employeesInStore":
                    columns.pop(1)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(4)
                    SQLdata = f'SELECT id,"firstName","lastName",store FROM "{table}"'
                case "deliveryMen":
                    columns.pop(1)
                    columns.pop(3)
                    columns.pop(3)
                    columns.pop(3)
                    SQLdata = f'SELECT id,"firstName","lastName",store FROM "{table}"'
                case "deliveries":
                    columns.pop(1)
                    columns.pop(1)
                    columns.pop(1)
                    SQLdata = f'SELECT id, date, distance FROM "{table}"'

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
                listbox.insert("end", f"{col1} {col2} {col3}")
                for data in dataColumns:
                    datTemp = []
                    data = data[1:-1]
                    data = data.split()
                    for dat in data:
                        dat = dat.strip(",")
                        dat = dat.strip("'")
                        datTemp.append(dat)
                    datTemp[0], datTemp[1], datTemp[2] = datTemp[0].ljust(16),datTemp[1].ljust(16),datTemp[2].ljust(16)
                    listbox.insert("end", f"{datTemp[0]} {datTemp[1]} {datTemp[2]}")



            elif len(columnNames)==4:
                col1, col2, col3, col4= columnNames[0].ljust(7), columnNames[1].ljust(12), columnNames[2].ljust(15), columnNames[3].ljust(7)
                listbox.insert("end", f"{col1} {col2} {col3} {col4}")
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

                    listbox.insert("end", f"{datTemp[0]} {datTemp[1]} {datTemp[2]} {datTemp[3]}")
            cursor.close()

        case "multi":
            import tkinter as tk
            objectsPickFrame = tk.Frame(pickFrame)
            objectsPickFrame.grid(row=4, column=0, sticky="nsew", padx=10, pady=(20,0))
            objectsPickFrame.columnconfigure(0, weight=1)
            objectsPickFrame.columnconfigure(1, weight=1)
            objectsPickFrame.columnconfigure(2, weight=1)
            objectsPickFrame.rowconfigure(0, weight=1)
            objectsPickFrame.rowconfigure(1, weight=2)

            objectsPickTitle = tk.Label(objectsPickFrame, text="Wybierz sklep", font=("Roboto", 10, "bold"))
            objectsPickTitle.grid(row=0, column=1, sticky="nsew")


            def pickOption():
                title = ""
                if table == "employeesInStore":
                    title = "Pracownicy dla: "
                elif table == "deliveryMen":
                    title = "Dostawcy dla: "
                return title
            objectsPickOptionTitle = tk.Label(objectsPickFrame, text=f"{pickOption()}")
            objectsPickOptionTitle.grid(row=1, column=0, sticky="nsew")




            def pickOptionWindow():
                pickWindow = tk.Toplevel()
                from library.additionalFiles.windowPosition import windowPos
                windowPos(root=pickWindow, windowWidth=900, windowHeight=500)
                pickWindow.title("Formularz wyboru")
                pickWindow.iconbitmap("assets/icons/form-18.ico")
                import os
                print(os.path.abspath(__file__))
            objectsPickOptionButton = tk.Button(objectsPickFrame, text="Wybierz", command=lambda: pickOptionWindow())
            objectsPickOptionButton.grid(row=1, column=1, sticky="nsew", padx=(7,10))

            #TODO zrob generowanie w nowym okienku opcji do wyboru z przyciskiem "Ackeptuj"
            objectsPickOptionEndTitle = tk.Label(objectsPickFrame, text="sklepu")
            objectsPickOptionEndTitle.grid(row=1, column=2, sticky="nsew")
            match table:
                case "employeesInStore":
                    pass
                case "deliveryMen":
                    pass

    from library.additionalFiles.guiFunctions import removeCursorSelection
    removeCursorSelection(listbox)

    #print(columnNames)
    #print(dataColumns)