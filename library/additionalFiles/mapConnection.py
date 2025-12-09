def mapConn(root):
    import tkintermapview

    map_widget = tkintermapview.TkinterMapView(root, corner_radius=0)
    map_widget.grid(row=0, column=0, sticky='nsew')
    map_widget.set_position(52.20,19.03)
    map_widget.set_zoom(6)

    return map_widget