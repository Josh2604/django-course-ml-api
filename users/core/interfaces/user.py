import abc


class UserInterface(abc.ABC):
    @abc.abstractmethod
    def get_user(self, user_id: int): raise NotImplementedError

    @abc.abstractmethod
    def get_all_users(self): raise NotImplementedError

    @abc.abstractmethod
    def create_user(self): raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user_id: int): raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user_id: int): raise NotImplementedError
