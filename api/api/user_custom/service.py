from django.core.exceptions import ValidationError

from api.user_custom.factory.user_factory import UserCustomFactory
from api.user_custom.repository.user_custom_repository import UserCustomRepository

from .models import UserCustom

INVESTOR = "investor"
OPERATOR = "operator"


class UserCustomService:
    @staticmethod
    def create_user(validated_data):
        """
        Lógica para crear un usuario basado en el rol.
        """
        try:
            validated_data["rol"]
            return UserCustomFactory.create_user(
                validated_data["username"],
                validated_data["dni"],
                validated_data["email"],
                validated_data["password"],
                validated_data["rol"]
            )

        except KeyError:

            return UserCustomFactory.create_user(
                validated_data["username"],
                validated_data["dni"],
                validated_data["email"],
                validated_data["password"],
            )

    @staticmethod
    def authenticate_user(username, password):
        """
        Autenticar un usuario basado en el nombre de usuario y la contraseña.
        """
        try:
            user = UserCustomRepository().get_by_username(username=username)
            if user is not None and user.check_password(password):
                return user
            return None
        except UserCustom.DoesNotExist:
            return None

    @staticmethod
    def get_all_users():
        """
        Obtener todos los usuarios.
        """
        return UserCustomRepository().get_all()
