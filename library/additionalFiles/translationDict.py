Dict = {
    "id": "ID",
    "address": "Adres",
    "firstName": "Imię",
    "lastName": "Nazwisko",
    "phoneNumber": "Numer telefonu",
    "workedHours": "Godziny pracy",
    "store": "Sklep",
    "addressFrom": "Adres wysyłki",
    "addressTo": "Adres odbioru",
    "deliveryMan": "Dostawcy",
    "date": "Data",
    "distance": "Dystans [km]",
    "age": "Wiek",
    "salary": "Pensja",
    "position": "Stanowisko",
    "owner": "Właściciel",
    "employeesNr": "Pracownicy"
}

DictReverse = {}

for eng, pol in Dict.items():
    DictReverse[pol] = eng