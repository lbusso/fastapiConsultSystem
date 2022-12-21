from fastapi import APIRouter, Depends
from starlette.requests import Request
from managers.auth_manager import oauth2_scheme, is_admin, is_student, is_consultor
from schemas.base import Consultbase
from managers.consult_manager import ConsultManager
from models.enums import State


router = APIRouter(prefix='/consult', tags=['Consults'])


@router.post('/create', dependencies=[Depends(oauth2_scheme), Depends(is_student)])
async def create_consult(request: Request, consult_data: Consultbase):
    user = request.state.user
    return await ConsultManager.create_consult(consult_data.dict(), user)


@router.get('/my-consults-list', dependencies=[Depends(oauth2_scheme)])
async def get_my_consults(request: Request):
    user = request.state.user
    return await ConsultManager.consults_list_by_user(user)


@router.get('/get_all', dependencies=[Depends(oauth2_scheme), Depends(is_consultor)])
async def get_all_consults():
    return await ConsultManager.get_all_consults()


@router.get('/search/{ticket}', dependencies=[Depends(oauth2_scheme)])
async def search_consult(request: Request, ticket: str):
    user = request.state.user
    return await ConsultManager.search_consult(ticket, user)


@router.put('/set-in-progress/{consult_id}', status_code=204)
async def set_in_progress(consult_id: int):
    await ConsultManager.change_status(State.in_progress, consult_id)

@router.put('/set-terminated/{consult_id}', status_code=204)
async def set_terminated(consult_id: int):
    await ConsultManager.change_status(State.terminated, consult_id)