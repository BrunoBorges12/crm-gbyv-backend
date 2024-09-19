from ninja import NinjaAPI
from .models import User, UserAdmin
from .schemas import UserClient, CreateUserAdmin,DefaultResponse
from ninja.errors import ValidationError
from ninja.errors import HttpError
from utils.create_response import create_response
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


@api.post("/create_user_admin", response={200: DefaultResponse, 403: DefaultResponse})
def create_user_cliente(request, payload: CreateUserAdmin):
    try:
        user_email =  User.objects.filter(email=payload.email).first()
        if user_email:
            return create_response(403,'Error','Email já existe',data=None)
        user = User.objects.create_user_default(
            first_name=payload.first_name,
            last_name=payload.last_name,
            email=payload.email,
            password=payload.password,
        )
        user_admin = UserAdmin(nivel=payload.nivel, user=user)
        user_admin.save()
        return create_response(200,'sucess','Usuario criado',payload.dict())
    except Exception as e:
        error_message = str(e)  
        raise HttpError(500,error_message)
# talvez mudar o nome  para nome mais comum 



@api.post('/login')
def login(request,payload):
    # busca o usuario de acordo com email passado 
    # verificar se usuario é admin ou client
    # criar jwt retorna para client consumi esse jwt que contera expiração
    pass
   