def removeCursorSelection(listbox):
    def deselect(uselessEvent):
        tempSelection = listbox.curselection()
        if tempSelection and 0 in tempSelection:
            listbox.after(1, lambda: listbox.selection_clear(0))


    listbox.bind("<<ListboxSelect>>", deselect)

def clearListbox(listbox):
    listbox.delete(0, "end")
    listbox.after(1, lambda: listbox.selection_clear(0))


selectedTableValue = ""
simpleSQLGenVal = ""
lastButtonClicked = None


def selectedTableFunc(param, button):
    global selectedTableValue
    global lastButtonClicked
    global simpleSQLGenVal

    currentBackgroundColor = button.cget("bg")

    if lastButtonClicked is not None and lastButtonClicked != button:
        lastButtonClicked.config(bg="SystemButtonFace")
    if currentBackgroundColor != "yellow":
        button.config(bg="yellow")
        selectedTableValue = param
        simpleSQLGenVal = param
        lastButtonClicked = button
    else:
        pass

    match param:
        case "sklepy":
            selectedTableValue = "sklepy"
            simpleSQLGenVal = "stores"
        case "pracownicy":
            selectedTableValue = "pracownicy"
            simpleSQLGenVal = "employeesInStore"
        case "dostawcy":
            selectedTableValue = "dostawcy"
            simpleSQLGenVal = "deliveryMen"
        case "dostawy":
            selectedTableValue = "dostawy"
            simpleSQLGenVal = "deliveries"
        case "pracownicy-w-sklepie":
            selectedTableValue = "pracownicy-w-sklepie"
        case "dostawcy-w-sklepie":
            selectedTableValue = "dostawcy-w-sklepie"