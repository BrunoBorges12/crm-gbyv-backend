from ninja import NinjaAPI
from typing import List
from .models import User
from .schemas import UserClient, CreateUser
from django.utils import timezone

api = NinjaAPI()


@api.get("/users/", response=UserClient)
def get_users(request):
    users = User.objects.all()
    return users


@api.post("/create_user_client")
def create_user_cliente(request, payload: CreateUser):
    # Cria o usuário sem definir a senha diretamente
    user = User.objects.create_user_default()
