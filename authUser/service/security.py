import jwt
from datetime import timedelta,datetime,timezone
from dotenv import load_dotenv
import os

load_dotenv() 
def create_access_token(
    id: str, token_expire: timedelta, subjectAdmin, subjectActive
) -> str:
    expire_data = datetime.now(timezone.utc) + token_expire
    encode = jwt.encode(
        {
            "id": id,
            "exp": expire_data,
            "subjectAdmin": subjectAdmin,
            "subjectActive": subjectActive,
        },
        os.getenv('SECRET_KEY'),
        algorithm="HS256",
    )
    return encode