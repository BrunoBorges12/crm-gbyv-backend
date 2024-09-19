from ninja import Schema
from pydantic import EmailStr
from typing import Optional


class BaseUser(Schema):
    first_name: str
    last_name: str
    password: str
    email: EmailStr


class UserClient(BaseUser):
    enterprise: str
    cpf: str
    email: str
    tel: str
    website: str
    positon_enterprise: str = None
    andress: str
    cep: str
    city: str
    state: str


class CreateUserAdmin(BaseUser):
    nivel: str

class DefaultResponse(Schema):
    status: str  # "success" ou "error"
    message: str  # Mensagem descritiva
    data: Optional[dict] = None  # Dados adicionais (opcional)
