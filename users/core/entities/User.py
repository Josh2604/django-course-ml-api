
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