from datetime import datetime, timedelta
from typing import Optional
from models.enums import RoleType

from decouple import config
import jwt
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from db import database
from models import user


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user['id'],
                "exp": datetime.utcnow() + timedelta(minutes=120)
            }
            return jwt.encode(payload, config('JWT_SECRET_KEY'), algorithm='HS256')
        except Exception as ex:
            raise ex



class CustomHTTPBearer(HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            payload = jwt.decode(res.credentials, config('JWT_SECRET_KEY'), algorithms=['HS256'])
            user_data = await database.fetch_one(user.select(user.c.id == payload['sub']))
            request.state.user = user_data
            return user_data
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token Expired")

        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid Token ")

oauth2_scheme = CustomHTTPBearer()


def is_student(request: Request):
    if not request.state.user['role'] == RoleType.student:
        raise HTTPException(403, "Forbidden")

def is_consultor(request: Request):
    if not request.state.user['role'] == RoleType.consultor:
        raise HTTPException(403, "Forbidden")

def is_admin(request: Request):
    if not request.state.user['role'] == RoleType.admin:
        raise HTTPException(403, "Forbidden")