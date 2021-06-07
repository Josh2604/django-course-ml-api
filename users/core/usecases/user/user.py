from users.core.repository.user.user import UserRepository


class UserCaseUser:
    @classmethod
    def get_users(cls):
        return UserRepository().get_all_users()

    @classmethod
    def get_user(cls, uid: int):
        return UserRepository().get_user(uid)

    @classmethod
    def create_user(cls):
        return UserRepository().create_user()

    @classmethod
    def update_user(cls):
        return UserRepository().update_user()

    @classmethod
    def delete_user(cls):
        return UserRepository().delete_user()