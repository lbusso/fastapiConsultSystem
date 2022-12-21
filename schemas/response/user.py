from schemas.base import UserBase


class UserRegisterOut(UserBase):
    first_name: str
    last_name: str
    phone: str


class UserList(UserBase):
    first_name: str
    last_name: str
    phone: str