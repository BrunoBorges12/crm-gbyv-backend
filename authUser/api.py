from ninja import NinjaAPI
from .models import User, UserAdmin
from .schemas import UserClient, CreateUserAdmin,DefaultResponse,UserLogin
from ninja.errors import ValidationError
from ninja.errors import HttpError
from utils.create_response import create_response
from .service.auth import create_admin_service
from django.db import transaction
from typing import cast
from datetime import timedelta
from .service.security import create_access_token
api = NinjaAPI()

# Trazer uma organização melhor? fazer uma função para mensagem padrão?
@api.exception_handler(ValidationError)
def validation_payload(request, exc: ValidationError):
    error = exc.errors[0]
    return api.create_response(
        request,
        {
            "status": "error",
            "error": [{"type": error["loc"][2], "message": error["msg"]}],
        },
        status=503,
    )


@api.get("/users/", response=UserClient)
def get_users(request):
    users = User.objects.all()
    return users


@api.post("/create_user_admin", response={201: DefaultResponse, 403: DefaultResponse})
def create_admin(request, payload: CreateUserAdmin):
    try:
        
        if User.objects.filter(email=payload.email).exists():
            return create_response(403,False,'Email já existe',data=None)
        with transaction.atomic():
            user = create_admin_service(payload)
            return create_response(201,True,'Usuario criado',data=cast(dict,user))
    except Exception as e:
        error_message = str(e)  
        raise HttpError(500,error_message)



@api.post('/login',response={200:DefaultResponse, 401:DefaultResponse})
def login(request,payload:UserLogin):
    user:User = User.objects.filter(email =payload.email).first()
    if user  and user.check_password(payload.password):
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
        access_token_expirer = timedelta(minutes=60 * 24 * 8)
        token = create_access_token(user_data['id'],access_token_expirer,False,True)
        return create_response(200,True,'Efetuado o login',data={"user_data":user_data,"token":token})
    return create_response(401,False,'Email ou senha icorreto',data=None)

   