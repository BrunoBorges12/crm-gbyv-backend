from ninja import NinjaAPI

from .models import User, UserAdmin,UserClient
from .schemas import  CreateUserAdmin,DefaultResponse,LoginDefault,CreateUserCLient
from ninja.errors import ValidationError
from ninja.errors import HttpError
from utils.create_response import create_response
from .service.auth import create_admin_service
from django.db import transaction
from typing import cast
from datetime import timedelta
from .service.security import create_access_token
api = NinjaAPI(urls_namespace="auth")

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
def login(request,payload:LoginDefault):
        # precisa refactoriza essa parte do login, verifica todos tipos de error e segurança
    user:User = User.objects.filter(email =payload.email).first()

    if user  and user.check_password(payload.password):
        if (payload.user_type == 'admin' and user.role != 'admin') or (payload.user_type == 'client' and user.role != 'client'):
            return create_response(401, False, 'Email ou senha incorretos', data=None) # faz check em qual login ele esta no client ou no admin
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "role":user.role
        }
        access_token_expirer = timedelta(minutes=20 )
        token = create_access_token(user_data['id'],access_token_expirer,user.role,True)
        return create_response(200,True,'Efetuado o login',data={"user_data":user_data,"token":token})
    return create_response(401,False,'Email ou senha icorreto',data=None)

@api.post('/create_user_client',response={201: DefaultResponse, 403: DefaultResponse}   )
def create_user_client(request,payload:CreateUserCLient):
    try:
        if User.objects.filter(email=payload.email).exists():
                    return create_response(403,False,'Email já existe',data=None)
        user_data = {
                'email': payload.email,
                'first_name': payload.first_name,
                'last_name': payload.last_name,
                'password': payload.password,
                'role': 'client'
            }
        with  transaction.atomic():         
            user_default  = User.objects.create_user_default(**user_data)
            user_client_data ={
                key:getattr(payload,key)
                for key  in vars(payload)
                if key  not in ['password', 'email', 'first_name', 'last_name']
            }
            print(user_client_data)
            user_client = UserClient.objects.create(user=user_default, **user_client_data)
            user_client.save()
            return create_response(201,True,'Usuario criado',data=cast(dict,payload.dict()))
    except Exception as e:
        error_message = str(e)  
        raise HttpError(500,error_message)
        

   