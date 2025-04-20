import datetime
import os

import jwt
from dotenv import load_dotenv

load_dotenv()


class CreateJWT:
    @staticmethod
    def create_token(username: str) -> str:
        """
        Gera um token JWT.
        """
        SECRET_KEY = os.getenv("SECRET_KEY")

        payload = {
            'user_id': 123,
            'username': username,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def validate_token(token: str, SECRET_KEY: str) -> dict:
        """
        Valida o token JWT.
        :param token: Token JWT a ser validado
        :return: Dados decodificados do token
        """
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            return decoded
        except jwt.ExpiredSignatureError:
            raise Exception("Token expirado!")
        except jwt.InvalidTokenError:
            raise Exception("Token inválido!")
