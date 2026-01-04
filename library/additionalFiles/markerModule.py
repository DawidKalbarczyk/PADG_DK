def markerSingleFunc(table):
    from library.engine import dbConnect
    if table != "deliveries":
        conn = dbConnect()
        cursor = conn.cursor()
        SQLmarkerData = f'SELECT "address" FROM "{table}" ORDER BY id;'
        cursor.execute(SQLmarkerData)
        data = cursor.fetchall()
        cursor.close()
        searchData = []
        for dat in data:
            dat = str(dat).replace("(","").replace(")","").replace("'","").replace(",","")
            dat = dat.split()[0]
            searchData.append(dat)

        coordinates = scrapFunc(searchData)
        markers = []
        from library.gui import Map
        for i,coords in enumerate(coordinates):
            marker = Map.set_marker(coords[0], coords[1], text=i)
            if coordinates == (0,0):
                marker.hide()
            markers.append(marker)
#TODO Dodać obsługę markerów dla deliveries (najlepiej trasa)
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
        # print(response_html.prettify())
        latitude = response_html.select('.latitude')
        longitude = response_html.select('.longitude')
        if len(latitude) > 1 and len(longitude) > 1:
            latitude = float(latitude[1].text.replace(",", "."))
            longitude = float(longitude[1].text.replace(",", "."))
            coordinates.append((latitude, longitude))
        else:
            print("Błąd w markerze!")
            coordinates.append((0,0))
    print(f"Latitude: {latitude}, Longitude: {longitude}")

    return coordinates
