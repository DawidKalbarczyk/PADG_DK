import tkinter as tk

def graphicUserInterface():
    root = tk.Tk()
    root.geometry('1025x600')
    root.title("System do zarządzania sklepami i pracownikami w mieście")
    root.config(bg="gray")

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

    titleLabel = (tk.Label(titleFrame, text="Narzędzia",
                           font=("Roboto", 10, "bold"), bg="yellow"))
    titleLabel.grid(row=0, column=0, pady=2, ipady=4, ipadx=4, sticky="nsew", columnspan=3)

    mainFrame = (tk.Frame(root, bg="gray"))
    mainFrame.grid(row=1, column=0, sticky="nsew")
    mainFrame.columnconfigure(0, weight=1)
    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    mainFrame.rowconfigure(2, weight=1)

    objectsFrame = tk.Frame(mainFrame, bg="blue", borderwidth=1, relief="solid")
    objectsFrame.grid(row=0, column=0, sticky="nsew")
    objectsLabel = tk.Label(objectsFrame, text="objLabel")  #######
    objectsLabel.pack()  # ######

    formFrame = tk.Frame(mainFrame, bg="red", borderwidth=1, relief="solid")
    formFrame.grid(row=1, column=0, sticky="nsew")
    formLabel = tk.Label(formFrame, text="formLabel")  ########
    formLabel.pack()  ######

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

    mapTitleFrame = tk.Frame(rightFrame, bg="red", borderwidth=1, relief="solid")
    mapTitleFrame.grid(row=0, column=1, sticky="nsew", columnspan=3)
    mapTitleFrame.columnconfigure(0, weight=1)
    mapTitleFrame.columnconfigure(1, weight=1)
    mapTitleFrame.columnconfigure(2, weight=1)

    mapTitleLabel = tk.Label(mapTitleFrame, text="Wygenerowanadwdwawa Mapa", font=("Roboto", 10, "bold"))
    mapTitleLabel.grid(row=0, column=1, pady=2, ipady=4, ipadx=4)


    mapFrame = tk.Frame(rightFrame, bg="yellow", borderwidth=1, relief="solid")
    mapFrame.grid(row=1, column=1, sticky="nsew", columnspan=3)

    mapLabel = tk.Label(mapFrame, text="mapLabel")  #####
    mapLabel.pack()  #######

    root.mainloop()

