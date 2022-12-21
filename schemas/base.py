from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class Consultbase(BaseModel):
    category: str
    text: str

class ReplyBase(BaseModel):
    text: str