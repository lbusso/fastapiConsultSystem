from fastapi import APIRouter
from schemas.request.user import UserRegisterIn, UserLogin
from managers.user_manager import UserManager


router = APIRouter(prefix='/auth', tags=['Authorization'])



@router.post('/register', status_code=201)
async def user_register(user_data: UserRegisterIn):
    token = await UserManager.register(user_data.dict())
    return {'token': token}



@router.post('/login', status_code=200)
async def user_login(user_data: UserLogin):
    token =await  UserManager.login(user_data.dict())
    return {'token': token}