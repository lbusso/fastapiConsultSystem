from asyncpg import UniqueViolationError
from fastapi import HTTPException
from managers.auth_manager import AuthManager
from db import database
from models import user, RoleType
from passlib.context import CryptContext




pwd_context =CryptContext(schemes='bcrypt', deprecated='auto')

class UserManager:
    @staticmethod
    async def register(user_data):
        user_data['password']= pwd_context.hash(user_data['password'])
        try:
            id_ = await database.execute(user.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email alrady exist")
        user_registred = await database.fetch_one(user.select(user.c.id == id_))
        return AuthManager.encode_token(user_registred)

    @staticmethod
    async def login(user_data):
        user_login = await database.fetch_one(user.select(user.c.email == user_data['email']))

        if not user_login:
            raise HTTPException(400, "Wrong email or password")

        elif not pwd_context.verify(user_data['password'], user_login['password']):
            raise HTTPException(400, "Wrong email or password")

        return AuthManager.encode_token(user_login)


    @staticmethod
    async def get_all_users():
        return await database.fetch_all(user.select())

    @staticmethod
    async def change_role(role: RoleType, user_id):
        await database.execute(user.update(user.c.id == user_id).values(role=role))
