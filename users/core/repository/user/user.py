from dependency_injector.wiring import Provide, inject
from users.core.entities.User import User
from users.core.interfaces.user import UserInterface
from users.infraestructure.dependencies.dependencies import (Container,
                                                             DBConnection)


class UserRepository(UserInterface):
    @inject
    def get_user(self, user_id: int, service: DBConnection = Provide[Container.service]):
        connection = None
        try:
            connection = service.create_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE id={}".format(user_id))
            user = cursor.fetchone()
            connection.close()
            return User(user[0], user[1], user[2], user[3]).userJSON()

        except Exception as error:
            print("error: ", error)
            raise Exception("Error inside UserRepository - get_user")
        finally:
            if connection is not None:
                connection.close()

    @inject
    def get_all_users(self, service: DBConnection = Provide[Container.service]):
        connection = None
        try:
            connection = service.create_connection()
            cursor = connection.cursor()
            cursor.execute("select * from Users")
            usersDict = []
            users = cursor.fetchall()
            connection.close()
            for row in users:
                # Two ways to do the same
                #usersDict.append({"id": row[0], "name": row[1], "apells": row[2], "age": row[3]})
                usersDict.append(User(row[0], row[1], row[2], row[3]).userJSON())

            return usersDict
        except Exception as error:
            print("error", error)
            raise RuntimeError
        finally:
            if connection is not None:
                connection.close()

    @inject
    def create_user(self, service: DBConnection = Provide[Container.service]):
        return "ok user created"

    @inject
    def update_user(self, user_id: int, service: DBConnection = Provide[Container.service]):
        return "Ok user updated"

    @inject
    def delete_user(self, user_id: int, service: DBConnection = Provide[Container.service]):
        return "Ok update user"
