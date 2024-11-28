from ninja import Schema
from pydantic import EmailStr
from typing import Optional


class UserLogin(Schema):
    email: str
    password: str

class LoginDefault(UserLogin):
    user_type:str


class BaseUser(UserLogin):
    first_name: str
    last_name: str


class UserClient(BaseUser):
    enterprise: str
    cpf: str
    email: str
    tel: str
    website: str
    positon_enterprise: Optional[str] = None
    andress: str
    cep: str
    city: str
    state: str


class CreateUserCLient(UserClient):
    pass

class CreateUserAdmin(BaseUser):
    business: str


class DefaultResponse(Schema):
    status: str  # "success" ou "error"
    message: str  # Mensagem descritiva
    data: Optional[dict] = None  # Dados adicionais (opcional)
