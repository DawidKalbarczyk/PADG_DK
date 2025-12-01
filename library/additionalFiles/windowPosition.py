def windowPos(root, windowWidth, windowHeight):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (windowWidth // 2)
    y = (screen_height // 2) - (windowHeight // 2)

    root.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
