markers = []
paths = []
def markerSingleFunc(table, condition=None):
    from library.engine import dbConnect
    conn = dbConnect()
    cursor = conn.cursor()
    circleColor = "darkred"
    outsideColor = "red"
    from library.gui import Map
    Map.delete_all_marker()
    global markers
    global paths
    markers = []
    paths = []
    if table != "deliveries":
        if table == "stores":
            SQLmarkerData = f'SELECT id,"address" FROM "{table}"'
            circleColor = "darkred"
            outsideColor = "red"

        elif table == "deliveryMen":
            SQLmarkerData = f'SELECT "lastName","address" FROM "{table}"'
            circleColor = "#a86b32"
            outsideColor = "#a87532"
        elif table == "employeesInStore":
            SQLmarkerData = f'SELECT "lastName","address" FROM "{table}"'
            circleColor = "#2f57ad"
            outsideColor = "#658adb"

        if condition:
            SQLmarkerData += f' WHERE {condition}'
        SQLmarkerData += 'ORDER BY id;'
        cursor.execute(SQLmarkerData)
        results = cursor.fetchall()
        names = []
        searchData = []
        for row in results:
            n = row[0]
            d = row[1]
            names.append(n)
            data = str(d).split(",")[0].strip().replace(" ","_")
            searchData.append(data)


        coordinates = scrapFunc(searchData)

        from library.gui import Map
        for name,coords in zip(names, coordinates):
            marker = Map.set_marker(coords[0], coords[1], text=name, marker_color_circle=circleColor, marker_color_outside=outsideColor)
            if coordinates == (0,0):
                marker.hide()
            markers.append(marker)
    elif table == "deliveries":
        SQLmarkerData = f'SELECT id,"addressFrom", "addressTo" FROM "{table}";'

        cursor.execute(SQLmarkerData)
        print(SQLmarkerData)
        results = cursor.fetchall()
        names = []
        searchData1 = []
        searchData2 = []
        for row in results:
            n = row[0]
            sd1 = row[1]
            sd2 = row[2]
            names.append(n)
            data1 = str(sd1).split()[0]
            data2 = str(sd2).split()[0]

            searchData1.append(data1)
            searchData2.append(data2)

        coordinatesFrom = scrapFunc(searchData1)
        coordinatesTo = scrapFunc(searchData2)

        from library.gui import Map

        for coords1, coords2 in zip(coordinatesFrom, coordinatesTo):

            if coords1 != (0,0):
                marker1 = Map.set_marker(coords1[0], coords1[1], marker_color_circle="darkred",
                                         marker_color_outside="red")
                markers.append(marker1)

            if coords2 != (0, 0):
                marker2 = Map.set_marker(coords2[0], coords2[1], marker_color_circle="#2ca30b", marker_color_outside="#6ad44c")
                markers.append(marker2)

        for name, coords1, coords2 in zip(names, coordinatesFrom, coordinatesTo):
            if coords1 != (0, 0) and coords2 != (0, 0):
                path = Map.set_path(
                    position_list=[coords1, coords2],
                    name=f"Trasa id: {name}",
                    width=3,
                    color="red")
                paths.append(path)

    conn.close()

#TODO dodać obsługę markerów dla tabel z warunkami
def scrapFunc(searchData):
    import requests
    from bs4 import BeautifulSoup

    naglowek = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0 Safari/537.36 "
                      "(+https://twojastrona.pl/contact)"
    }
    coordinates = []
    for data in searchData:
        url: str = f"https://pl.wikipedia.org/wiki/{data}"
        response = requests.get(url, headers=naglowek)
        response_html = BeautifulSoup(response.text, "html.parser")

        latitude = response_html.select('.latitude')
        longitude = response_html.select('.longitude')
        if len(latitude) > 1 and len(longitude) > 1:
            latitude = float(latitude[1].text.replace(",", "."))
            longitude = float(longitude[1].text.replace(",", "."))
            coordinates.append((latitude, longitude))
            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("Błąd w markerze!")
            coordinates.append((0,0))


    return coordinates
