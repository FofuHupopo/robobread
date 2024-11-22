import jwt
import requests
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Проверка токена через auth микросервис
        response = requests.get(f"{settings.AUTH_SERVICE_URL}/verify", headers={"Authorization": f"Bearer {token}"})
        if response.status_code != 200:
            raise HTTPException(status_code=403, detail="Invalid authentication credentials")
        return response.json()  # предположим, что возвращается информация о пользователе
    except Exception as e:
        raise HTTPException(status_code=403, detail="Invalid authentication credentials")
