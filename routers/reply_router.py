from typing import List

from fastapi import APIRouter, Depends
from managers.reply_manager import ReplyManager
from managers.auth_manager import oauth2_scheme
from schemas.base import ReplyBase

router = APIRouter(tags=['Reply'], prefix='/reply')

@router.post('/create/{consult_id}', dependencies=[Depends(oauth2_scheme)])
async def create_reply(reply_data: ReplyBase, consult_id: int):
    return await ReplyManager.create_reply(reply_data.dict(), consult_id)

@router.get('/get/{consult_id}', dependencies=[Depends(oauth2_scheme)])
async def create_reply(consult_id: int):
    return await ReplyManager.get_reply(consult_id)