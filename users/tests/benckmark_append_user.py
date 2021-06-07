import timeit


class User:
    def __init__(self, id: int, name: str, apells: str, age: int):
        if type(id) is not int:
            raise TypeError("incorrect value for int")
        self.__id = id
        self.__name = name
        self.__apells = apells
        self.__age = age

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, d):
        if not d: raise Exception("description cannot be empty")
        self.__id = d

    def userJSON(self):
        return {"id": self.__id, "name": self.__name, "apells": self.__apells, "age": self.__age}


users = [
    [
        1,
        "Juan",
        "Alberto Quintero",
        24
    ],
    [
        2,
        "Juan",
        "Antonio",
        20
    ],
    [
        3,
        "Jose",
        "Damian",
        30
    ],
    [
        4,
        "Oscar",
        "Hernandez",
        31
    ],
    [
        5,
        "Gillermo",
        "De la luz",
        26
    ],
    [
        6,
        "Santiago",
        "Gerrero",
        27
    ],
    [
        7,
        "Armando",
        "Damian",
        22
    ],
    [
        8,
        "Pedro",
        "Damian",
        29
    ],
    [
        9,
        "Berenice",
        "Matiaz",
        27
    ]
]


@profile
def appendingUsers():
    users_dict = []
    for row in users:
        users_dict.append({"id": row[0], "name": row[1], "apells": row[2], "age": row[3]})

    print(users_dict)


@profile
def appendingUsersWithClass():
    users_dict = []
    for row in users:
        users_dict.append(User(row[0], row[1], row[2], row[3]).userJSON())
    print(users_dict)


appendingUsers()
appendingUsersWithClass()
