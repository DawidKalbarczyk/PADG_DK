def removeCursorSelection(listbox):
    def deselect(uselessEvent):
        tempSelection = listbox.curselection()
        if tempSelection and 0 in tempSelection:
            listbox.after(1, lambda: listbox.selection_clear(0))


    listbox.bind("<<ListboxSelect>>", deselect)
