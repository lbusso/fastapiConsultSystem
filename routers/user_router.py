from typing import List

from fastapi import APIRouter, Depends
from managers.user_manager import UserManager
from managers.auth_manager import oauth2_scheme
from models.enums import RoleType
from schemas.response.user import UserList

router = APIRouter(prefix='/users', tags=['Users'])



@router.get('/get_all', dependencies=[Depends(oauth2_scheme)], response_model=List[UserList])
async def get_users():
    return await UserManager.get_all_users()

@router.put('/set-admin/{consult_id}', status_code=204)
async def set_in_progress(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)

@router.put('/set-consultor/{consult_id}', status_code=204)
async def set_terminated(user_id: int):
    await UserManager.change_role(RoleType.consultor, user_id)