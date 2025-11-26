import tkinter as tk
def graphicUserInterface():
    root = tk.Tk()
    root.geometry('1025x600')
    root.title("System do zarządzania sklepami i pracownikami w mieście")
    root.iconbitmap('assets/icons/app-icon.ico')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    # root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    leftFrame = tk.Frame(root)
    leftFrame.grid(row=0, column=0, sticky="nsew")
    # leftFrame.columnconfigure(0, weight=1)
    leftFrame.rowconfigure(1, weight=1)
    leftFrame.columnconfigure(0, weight=1)
    leftFrame.columnconfigure(1, weight=1)
    leftFrame.columnconfigure(2, weight=1)


    titleFrame = tk.Frame(leftFrame, borderwidth=1, relief="solid")
    titleFrame.grid(row=0, column=0, sticky="ew", columnspan=3)
    titleFrame.columnconfigure(0, weight=1)
    titleFrame.columnconfigure(1, weight=1)
    titleFrame.columnconfigure(2, weight=1)
    titleFrame.columnconfigure(3, weight=1)

    titleLabel = (tk.Label(titleFrame, text="Narzędzia",
                           font=("Roboto", 12, "bold")))
    titleLabel.grid(row=0, column=0, pady=2, ipady=4, ipadx=4, sticky="nsew", columnspan=3)

    imageTools = tk.PhotoImage(file="assets/icons/tools.png")
    imageTools = imageTools.subsample(17, 17)
    imageToolsLabel = tk.Label(titleFrame, image=imageTools)
    imageToolsLabel.grid(row=0, column=3)

    mainFrame = (tk.Frame(root))
    mainFrame.grid(row=1, column=0, sticky="nsew")
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    mainFrame.rowconfigure(2, weight=1)




    objectsFrame = tk.Frame(mainFrame, borderwidth=1, relief="solid")
    objectsFrame.grid(row=0, column=0, sticky="nsew")
    objectsFrame.columnconfigure(0, weight=1)
    objectsFrame.rowconfigure(0, weight=1)
    objectsFrame.rowconfigure(1, weight=9)
    objectsLabel = tk.Label(objectsFrame, text="Lista obiektów")  #######
    objectsLabel.grid(row=0, column=0) # ######
    objectsList = tk.Listbox(objectsFrame, borderwidth=3, relief="groove")
    objectsList.grid(row=1, column=0, sticky="new", padx=10, pady=10)




    formFrame = tk.Frame(mainFrame, bg="red", borderwidth=1, relief="solid")
    formFrame.grid(row=1, column=0, sticky="nsew")
    formFrame.columnconfigure(0, weight=1)
    formFrame.columnconfigure(1, weight=1)
    formFrame.columnconfigure(2, weight=1)
    formFrame.rowconfigure(0, weight=1)
    formFrame.rowconfigure(1, weight=9)

    formTitleFrame = tk.Frame(formFrame)
    formTitleFrame.grid(row=0, column=0, sticky="nsew", columnspan=3)
    formTitleFrame.columnconfigure(0, weight=1)
    formTitleFrame.columnconfigure(1, weight=1)
    formTitleFrame.columnconfigure(2, weight=1)
    formLabel = tk.Label(formFrame, text="Formularz")  ########
    formLabel.grid(row=0, column=1)


    formEntryFrame = tk.Frame(formFrame)
    formEntryFrame.grid(row=1, column=0, sticky="nsew", columnspan=3)
    formEntryFrame.columnconfigure(0, weight=1)
    formEntryFrame.columnconfigure(1, weight=3)
    formEntryFrame.rowconfigure(0, weight=1)
    formEntryFrame.rowconfigure(1, weight=1)
    formEntryFrame.rowconfigure(2, weight=1)
    formEntryFrame.rowconfigure(3, weight=1)

    formEntryName = tk.Label(formEntryFrame, text="Imię: ")
    formEntryName.grid(row=0, column=0)
    formEntryNameValue = tk.Entry(formEntryFrame)
    formEntryNameValue.grid(row=0, column=1, sticky="ew", padx=(0,20))

    formEntryName = tk.Label(formEntryFrame, text="Lokalizacja: ")
    formEntryName.grid(row=1, column=0)
    formEntryNameValue = tk.Entry(formEntryFrame)
    formEntryNameValue.grid(row=1, column=1, sticky="ew", padx=(0,20))

    formEntryPosts = tk.Label(formEntryFrame, text="Posts: ")
    formEntryPosts.grid(row=2, column=0)
    formEntryPostsValue = tk.Entry(formEntryFrame)
    formEntryPostsValue.grid(row=2, column=1, sticky="ew", padx=(0,20))

    formEntryIMG = tk.Label(formEntryFrame, text="IMG: ")
    formEntryIMG.grid(row=3, column=0)
    formEntryIMGValue = tk.Entry(formEntryFrame)
    formEntryIMGValue.grid(row=3, column=1, sticky="ew", padx=(0,20))















    objectDescriptionFrame = tk.Frame(mainFrame, bg="green", borderwidth=1, relief="solid")
    objectDescriptionFrame.grid(row=2, column=0, sticky="nsew")
    objectDescriptionLabel = tk.Label(objectDescriptionFrame, text="objDescriptionLabel")  #######
    objectDescriptionLabel.pack()  ######




    rightFrame = tk.Frame(root, borderwidth=1, relief="solid")
    rightFrame.grid(row=0, column=1, sticky="nsew", rowspan=2, columnspan=3)
    rightFrame.columnconfigure(0, weight=0)
    rightFrame.rowconfigure(1, weight=1)
    rightFrame.columnconfigure(1, weight=1)
    rightFrame.columnconfigure(2, weight=1)

    mapTitleFrame = tk.Frame(rightFrame, borderwidth=1, relief="solid")
    mapTitleFrame.grid(row=0, column=1, sticky="nsew", columnspan=3)
    mapTitleFrame.columnconfigure(0, weight=1)
    mapTitleFrame.columnconfigure(1, weight=1)
    mapTitleFrame.columnconfigure(2, weight=1)
    mapTitleFrame.columnconfigure(3, weight=1)

    mapTitleLabel = tk.Label(mapTitleFrame, text="Wygenerowana Mapa", font=("Roboto", 12, "bold"))
    mapTitleLabel.grid(row=0, column=0, pady=2, ipady=4, ipadx=4, columnspan=3)

    imageMap = tk.PhotoImage(file="assets/icons/map.png")
    imageMap = imageMap.subsample(17, 17)
    imageMapLabel = tk.Label(mapTitleFrame, image=imageMap)
    imageMapLabel.grid(row=0, column=3)


    mapFrame = tk.Frame(rightFrame, bg="yellow", borderwidth=1, relief="solid")
    mapFrame.grid(row=1, column=1, sticky="nsew", columnspan=3)

    mapLabel = tk.Label(mapFrame, text="mapLabel")  #####
    mapLabel.pack()  #######

    root.mainloop()

