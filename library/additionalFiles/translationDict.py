Dict = {
    "id": "ID",
    "address": "ADRES",
    "firstName": "IMIĘ",
    "lastName": "NAZWISKO",
    "phoneNumber": "NUMER TELEFONU",
    "workedHours": "GODZINY PRACY",
    "store": "SKLEP",
    "addressFrom": "ADRES WYSYŁKI",
    "addressTo": "ADRES ODBIORU",
    "deliveryMan": "DOSTAWCY",
    "date": "DATA",
    "distance": "DYSTANS [km]",
    "age": "WIEK",
    "salary": "PENSJA",
    "position": "STANOWISKO",
    "owner": "WŁAŚCICIEL",
    "employeesNr": "PRACOWNICY"
}

DictReverse = {}

for eng, pol in Dict.items():
    DictReverse[pol] = eng