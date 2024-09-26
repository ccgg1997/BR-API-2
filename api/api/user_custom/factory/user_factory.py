from api.user_custom.repository.user_custom_repository import UserCustomRepository


class UserCustomFactory:
    @staticmethod
    def create_user(username, dni, email, password, rol='user'):
        return UserCustomRepository().create_user(username, dni, rol, email, password)
