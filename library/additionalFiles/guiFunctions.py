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
lastButtonClicked = None


def selectedTableFunc(param, button):
    global selectedTableValue
    global lastButtonClicked

    currentBackgroundColor = button.cget("bg")

    if lastButtonClicked is not None and lastButtonClicked != button:
        lastButtonClicked.config(bg="SystemButtonFace")
    if currentBackgroundColor != "yellow":
        button.config(bg="yellow")
        selectedTableValue = param
        lastButtonClicked = button
    else:
        pass

    match param:
        case "sklepy":
            selectedTableValue = "sklepy"
        case "pracownicy":
            selectedTableValue = "pracownicy"
        case "dostawcy":
            selectedTableValue = "dostawcy"
        case "dostawy":
            selectedTableValue = "dostawy"
        case "pracownicy-w-sklepie":
            selectedTableValue = "pracownicy-w-sklepie"
        case "dostawcy-w-sklepie":
            selectedTableValue = "dostawcy-w-sklepie"