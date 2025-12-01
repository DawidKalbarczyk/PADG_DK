import tkinter as tk
from library.additionalFiles.windowPosition import windowPos
from library.additionalFiles.closeWholeProgram import closeProgram
def graphicUserInterface(appRoot):
    table = "employeesInStore"

    appRoot.withdraw()
    root = tk.Toplevel(appRoot)
    windowPos(root=root, windowWidth=1025, windowHeight=700)
    root.title("System do zarzadzania sklepami i pracownikami w miescie")
    root.iconbitmap('assets/icons/app-icon.ico')
    root.protocol("WM_DELETE_WINDOW", lambda: closeProgram(root, appRoot))
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    root.columnconfigure(2, weight=2)
    root.columnconfigure(3, weight=2)

    # root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    leftFrame = tk.Frame(root, borderwidth=1, relief="solid")
    leftFrame.grid(row=0, column=0, sticky="nsew", ipadx=10, pady=(0,15))
    # leftFrame.columnconfigure(0, weight=1)
    leftFrame.rowconfigure(1, weight=1)
    leftFrame.columnconfigure(0, weight=1)
    leftFrame.columnconfigure(1, weight=1)
    leftFrame.columnconfigure(2, weight=1)


    titleFrame = tk.Frame(leftFrame)
    titleFrame.grid(row=0, column=0, sticky="ew", columnspan=3, padx=(2,3))
    titleFrame.columnconfigure(0, weight=1)
    titleFrame.columnconfigure(1, weight=1)
    titleFrame.columnconfigure(2, weight=1)
    titleFrame.columnconfigure(3, weight=1)

    titleLabel = (tk.Label(titleFrame, text="Narzedzia",
                           font=("Roboto", 12, "bold")))
    titleLabel.grid(row=0, column=0, pady=2, ipady=4, ipadx=4, sticky="nsew", columnspan=3)

    imageTools = tk.PhotoImage(file="assets/icons/tools.png")
    imageTools = imageTools.subsample(17, 17)
    imageToolsLabel = tk.Label(titleFrame, image=imageTools)
    imageToolsLabel.image = imageTools
    imageToolsLabel.grid(row=0, column=3)


    mainFrame = (tk.Frame(root))
    mainFrame.grid(row=1, column=0, sticky="nsew")
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    mainFrame.rowconfigure(2, weight=1)




    objectsFrame = tk.Frame(mainFrame)
    objectsFrame.grid(row=0, column=0, sticky="new")
    objectsFrame.columnconfigure(0, weight=1)
    objectsFrame.rowconfigure(0, weight=1)
    objectsFrame.rowconfigure(1, weight=1)
    objectsFrame.rowconfigure(2, weight=9)
    objectsFrame.rowconfigure(3, weight=1)
    objectsFrame.rowconfigure(4, weight=1)
    objectsLabel = tk.Label(objectsFrame, text="Lista obiektÃ³w", font=("Roboto", 10, "bold"))  #######
    objectsLabel.grid(row=0, column=0) # ######

    objectsButtonsFrame = tk.Frame(objectsFrame)
    objectsButtonsFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    objectsButtonsFrame.columnconfigure(0, weight=1)
    objectsButtonsFrame.columnconfigure(1, weight=1)
    objectsButtonsFrame.columnconfigure(2, weight=1)
    objectsButtonsFrame.columnconfigure(3, weight=1)

    objectsStoreListButton = tk.Button(objectsButtonsFrame, text = "Sklepy")
    objectsStoreListButton.grid(row=0, column=0, sticky="ew", )

    objectsEmployeeButton = tk.Button(objectsButtonsFrame, text = "Pracownicy")
    objectsEmployeeButton.grid(row=0, column=1, sticky="ew",padx=5)

    objectsDeliveriesButton = tk.Button(objectsButtonsFrame, text = "Dostawy")
    objectsDeliveriesButton.grid(row=0, column=2, sticky="ew")

    objectsDeliveryMen = tk.Button(objectsButtonsFrame, text = "Dostawcy")
    objectsDeliveryMen.grid(row=0, column=3, sticky="ew", padx=(5,0))

    objectsList = tk.Listbox(objectsFrame, borderwidth=3, relief="groove")
    objectsList.grid(row=2, column=0, sticky="new", padx=10, pady=10)




    from library.additionalFiles.newWindow import newWindow

    objectsCommandButtonsFrame = tk.Frame(objectsFrame)
    objectsCommandButtonsFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
    objectsCommandButtonsFrame.columnconfigure(0, weight=1)
    objectsCommandButtonsFrame.columnconfigure(1, weight=1)
    objectsCommandButtonsFrame.columnconfigure(2, weight=1)


    objectsCommandAddButton = tk.Button(objectsCommandButtonsFrame, text = "Dodaj rekord", command = lambda: newWindow("add", objectsFrame, table))
    objectsCommandAddButton.grid(row=0, column=0, sticky="ew")

    objectsCommandEditButton = tk.Button(objectsCommandButtonsFrame, text = "Edytuj rekord", command = lambda: newWindow("edit", objectsFrame))
    objectsCommandEditButton.grid(row=0, column=1, sticky="ew", padx=5)

    objectsCommandDeleteButton = tk.Button(objectsCommandButtonsFrame, text = "Usun„ rekord")#, command = lambda: deleteRecord())
    objectsCommandDeleteButton.grid(row=0, column=2, sticky="ew")

    objectsShowAllButton = tk.Button(objectsFrame, text = "PokaÅ¼ szczegÃ³Å‚y")
    objectsShowAllButton.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

    rightFrame = tk.Frame(root, borderwidth=1, relief="solid", )
    rightFrame.grid(row=0, column=1, sticky="nsew", rowspan=2, columnspan=3)
    rightFrame.columnconfigure(0, weight=0)
    rightFrame.rowconfigure(1, weight=1)
    rightFrame.columnconfigure(1, weight=1)
    rightFrame.columnconfigure(2, weight=1)

    mapTitleFrame = tk.Frame(rightFrame)
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
    imageMapLabel.image = imageMap
    imageMapLabel.grid(row=0, column=3)

    mapFrame = tk.Frame(rightFrame, bg="yellow", borderwidth=1, relief="solid")
    mapFrame.grid(row=1, column=1, sticky="nsew", columnspan=3, pady=(1, 0))
    mapFrame.columnconfigure(0, weight=1)
    mapFrame.rowconfigure(0, weight=1)










    from library.additionalFiles.mapConnection import mapConn

    Map = mapConn(root=mapFrame)


"""
    formFrame = tk.Frame(mainFrame, borderwidth=1, relief="solid")
    formFrame.grid(row=1, column=0, sticky="nsew", padx=(0,0))
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
    formLabel = tk.Label(formFrame, text="Formularz", font=("Roboto", 10, "bold"))  ########
    formLabel.grid(row=0, column=1)


    formEntryFrame = tk.Frame(formFrame)
    formEntryFrame.grid(row=1, column=0, sticky="nsew", columnspan=3)
    formEntryFrame.columnconfigure(0, weight=1)
    formEntryFrame.columnconfigure(1, weight=3)
    formEntryFrame.rowconfigure(0, weight=1)
    formEntryFrame.rowconfigure(1, weight=1)
    formEntryFrame.rowconfigure(2, weight=1)
    formEntryFrame.rowconfigure(3, weight=1)

    formEntryName = tk.Label(formEntryFrame, text="ImiÄ™: ")
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

    formEntryIMG = tk.Label(formEntryFrame, text="Image Source: ")
    formEntryIMG.grid(row=3, column=0)
    formEntryIMGValue = tk.Entry(formEntryFrame)
    formEntryIMGValue.grid(row=3, column=1, sticky="ew", padx=(0,20))















    objectDescriptionFrame = tk.Frame(mainFrame)
    objectDescriptionFrame.grid(row=2, column=0, sticky="nsew")
    objectDescriptionFrame.columnconfigure(0, weight=1)
    objectDescriptionFrame.columnconfigure(1, weight=1)
    objectDescriptionFrame.rowconfigure(1, weight=1)
    objectDescriptionFrame.rowconfigure(2, weight=1)
    objectDescriptionFrame.rowconfigure(3, weight=1)
    objectDescriptionFrame.rowconfigure(4, weight=1)
    objectDescriptionLabel = tk.Label(objectDescriptionFrame, text="SzczegÃ³Å‚y obiektu", font=("Roboto", 10, "bold"))  #######
    objectDescriptionLabel.grid(row=0, column=0, columnspan=2)  ######
    descriptionName = tk.Label(objectDescriptionFrame, text="ImiÄ™: ")
    descriptionName.grid(row=1, column=0, sticky="nsew")
    descriptionNameValue = tk.Entry(objectDescriptionFrame)
    descriptionNameValue.grid(row=1, column=1, sticky="ew", padx=(0,20))
    descriptionLocation = tk.Label(objectDescriptionFrame, text="Pozycja obiektu: ")
    descriptionLocation.grid(row=2, column=0, sticky="nsew")
    descriptionLocationValue = tk.Entry(objectDescriptionFrame)
    descriptionLocationValue.grid(row=2, column=1, sticky="ew", padx=(0,20))
    descriptionPosts = tk.Label(objectDescriptionFrame, text="Posts: ")
    descriptionPosts.grid(row=3, column=0, sticky="nsew")
    descriptionPostsValue = tk.Entry(objectDescriptionFrame)
    descriptionPostsValue.grid(row=3, column=1, sticky="ew", padx=(0,20))
    descriptionIMG = tk.Label(objectDescriptionFrame, text="Image Source: ")
    descriptionIMG.grid(row=4, column=0, sticky="nsew")
    descriptionIMGValue = tk.Entry(objectDescriptionFrame)
    descriptionIMGValue.grid(row=4, column=1, sticky="ew", padx=(0,20))

"""


