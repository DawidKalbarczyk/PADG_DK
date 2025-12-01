import tkinter as tk
from library.additionalFiles.windowPosition import windowPos
from library.additionalFiles.closeWholeProgram import closeProgram
allowedToLogin = False
def login(appRoot):
    appRoot.withdraw()
    root = tk.Toplevel(appRoot)
    windowPos(root=root, windowWidth=400, windowHeight=200)
    root.title("Okno logowania")
    root.iconbitmap("assets/icons/key.ico")
    root.protocol("WM_DELETE_WINDOW", lambda: closeProgram(root, appRoot))
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)

    loginTextFrame = tk.Frame(root)
    loginTextFrame.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    loginTextFrame.columnconfigure(0, weight=1)
    loginTextFrame.columnconfigure(1, weight=1)
    loginTextFrame.columnconfigure(2, weight=1)

    loginTextLabel = tk.Label(loginTextFrame, text="Wpisz dane logowania", font=("Roboto", 12))
    loginTextLabel.grid(row=0, column=1)

    loginValuesFrame = tk.Frame(root)
    loginValuesFrame.grid(row=1, column=0, rowspan=2, columnspan=3, sticky="nsew", padx=10, pady=10)
    loginValuesFrame.columnconfigure(0, weight=1)
    loginValuesFrame.columnconfigure(1, weight=1)
    loginValuesFrame.columnconfigure(2, weight=1)
    loginValuesFrame.rowconfigure(0, weight=1)
    loginValuesFrame.rowconfigure(1, weight=1)

    loginValuesLoginText = tk.Label(loginValuesFrame, text="Id pracownika: ")
    loginValuesLoginText.grid(row=0, column=0)

    loginValuesLoginValue = tk.Entry(loginValuesFrame)
    loginValuesLoginValue.grid(row=0, column=1, columnspan=2, sticky="ew", padx=(0,40), pady=10)

    loginValuesPasswordText = tk.Label(loginValuesFrame, text="Password: ")
    loginValuesPasswordText.grid(row=1, column=0)

    loginValuesPasswordValue = tk.Entry(loginValuesFrame, show="*")
    loginValuesPasswordValue.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(0,40), pady=10)


    loginButtonsFrame = tk.Frame(root)
    loginButtonsFrame.grid(row=3, column=1, columnspan=2, sticky="nsew", padx=10, pady=10)

    loginButtonsAccept = tk.Button(loginButtonsFrame, text="Logowanie", command=lambda: get_values(loginValuesLoginValue, loginValuesPasswordValue, root))
    loginButtonsAccept.grid(row=0, column=0, padx=10, pady=10)

    loginButtonsDeny = tk.Button(loginButtonsFrame, text="WyjdÅº", command=appRoot.destroy)
    loginButtonsDeny.grid(row=0, column=1, padx=10, pady=10)
    appRoot.wait_window(root)  # czeka az zamknie okno
    return allowedToLogin

def get_values(loginEntry, passwordEntry, root):
    global allowedToLogin
    loginValue = loginEntry.get()
    passwordValue = passwordEntry.get()


    from library.engine import dbConnect
    SQL = f'SELECT id, password FROM "employeesInStore" WHERE id = {loginValue}'
    cursor = dbConnect().cursor()
    cursor.execute(SQL)
    result = cursor.fetchone()

    if result is None:
        alert = tk.Toplevel(root)
        windowPos(root=alert, windowWidth=350, windowHeight=100)
        alert.title("Error")
        alert.iconbitmap("assets/icons/error-icon-4.ico")
        alert.columnconfigure(0, weight=1)
        alert.columnconfigure(1, weight=1)
        alert.columnconfigure(2, weight=1)
        alert.rowconfigure(0, weight=1)
        alert.rowconfigure(1, weight=1)

        alertText = tk.Label(alert, text="Wprowadzono bledne dane logowania!")
        alertText.grid(row=0, column=1, padx=10, pady=10)

        alertButton = tk.Button(alert, text="Zamknij", command=alert.destroy)
        alertButton.grid(row=1, column=1, padx=10, pady=10)
    else:
        dataLogin, dataPassword = result
        if int(loginValue) == dataLogin and passwordValue == dataPassword:
            allowedToLogin = True
            root.destroy()

        else:
            alert = tk.Toplevel(root)
            windowPos(root=alert, windowWidth=350, windowHeight=100)
            alert.title("Error")
            alert.iconbitmap("assets/icons/error-icon-4.ico")
            alert.columnconfigure(0, weight=1)
            alert.columnconfigure(1, weight=1)
            alert.columnconfigure(2, weight=1)
            alert.rowconfigure(0, weight=1)
            alert.rowconfigure(1, weight=1)

            alertText = tk.Label(alert, text="Wprowadzono bledne dane logowania!")
            alertText.grid(row=0, column=1, padx=10, pady=10)

            alertButton = tk.Button(alert, text="Zamknij", command=alert.destroy)
            alertButton.grid(row=1, column=1, padx=10, pady=10)

