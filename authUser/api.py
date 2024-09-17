from ninja import NinjaAPI
from typing import List
from .models import User
from .schemas import UserClient,CreateUser

api = NinjaAPI()

@api.get("/users/", response=UserClient)
def get_users(request):
    users = User.objects.all()
    return users

@api.post('/create_user')
def create_user(request,payload:CreateUser):
    user = User.objects.create()
    print(user)     
    return  payload