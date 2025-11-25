def updateAllEmployees(employeesInStore):
    employeesAllStores: list = []
    for dictionary in employeesInStore:
        employeesInStore.append(dictionary)
    return employeesAllStores


stores: list  = [{
    "id": 1,
    "address": "Warszawska 39",
    "owner": "Mateusz Sobiecki",
    "employeesNr": 13,
    "phoneNumber": "683-172-929"
}]

employeesInStore: list = [{
    "id": 1,
    "age": 20,
    "firstName": "John",
    "lastName": "Doe",
    "salary": 8190.01,
    "position": "Kasjer",
    "phoneNumber": "683-172-929",
    "address": "Warszawska 19",
    "workedHours": 168,
    "store": 1
}]

employeesAllStores = updateAllEmployees(employeesInStore)





deliveryMenInStore: list = [{
    "id": 1,
    "address": "Warszawska 99",
    "firstName": "Johnathan",
    "lastName": "Pork",
    "phoneNumber": "683-172-929",
    "salary": 17290.00,
    "workedHours": 168
}]

deliveryMenAllStores = updateAllEmployees(deliveryMenInStore)

deliveries: list = [{
    "id": 1,
    "addressFrom": "Warszawska 39",
    "addressTo": "Warszawska 39",
    "deliveryMan": 1,
    "date": "2025-11-25"
}]