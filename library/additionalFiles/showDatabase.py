from ..engine import dbConnect
def showDatabase(table, listbox):
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
        case "deliveryMenInStore":
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
   # print(tempText)

    #print(columnNames)
    #print(dataColumns)