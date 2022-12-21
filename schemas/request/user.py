from pydantic import BaseModel

from schemas.base import UserBase


class UserRegisterIn(UserBase):
    password: str
    first_name: str
    last_name: str
    phone: str


class UserLogin(UserBase):
    password: str