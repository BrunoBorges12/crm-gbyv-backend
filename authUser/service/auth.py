from  ..models import User,UserAdmin
from dataclasses import dataclass
from typing import TypedDict

class UserResponse(TypedDict):
    user_id: str
    email: str

def create_admin_service(payload) -> UserResponse:
    
        user = User.objects.create_user_default(
                first_name=payload.first_name,
                last_name=payload.last_name,
                email=payload.email,
                password=payload.password,
            )
        user_admin = UserAdmin(nivel=payload.nivel, user=user)
        user_admin.save()
        return {"user_id": user.id, "email": user.email}  # Retornando informações úteis

