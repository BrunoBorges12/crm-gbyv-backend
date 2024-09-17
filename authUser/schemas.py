from ninja import Schema

class BaseUser(Schema):
    first_name: str
    last_name: str
    admin: bool
        
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
    
class CreateUser(BaseUser):
    password:str
    

