import os
import jwt
from ninja.security import HttpBearer

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        # Pega o secret_key da variável de ambiente
        secret_key = os.getenv('SECRET_KEY')
        
        try:
            # Decodifica o token usando o secret_key
            decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
            # Retorna o token decodificado ou o ID do usuário, por exemplo
            return decoded_token
        except jwt.ExpiredSignatureError:
            # Caso o token tenha expirado
            return None
        except jwt.InvalidTokenError:
            # Caso o token seja inválido
            return None
