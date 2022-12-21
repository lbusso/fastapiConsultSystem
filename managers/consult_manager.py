from db import database
from models.consult import consult
from models.enums import State
from uuid import uuid4

class ConsultManager:
    @staticmethod
    async def create_consult(consult_data, user):
        consult_data['user_id'] = user['id']
        ticket = str(uuid4())
        consult_data['ticket'] = ticket[:10]
        consult_data['state'] = State.pending.name
        id_ = await database.execute(consult.insert().values(consult_data))
        return await database.fetch_one(consult.select(consult.c.id == id_))

    @staticmethod
    async def consults_list_by_user(user):
        return await database.fetch_all(consult.select(consult.c.user_id == user['id']))

    @staticmethod
    async def get_all_consults():
        return await database.fetch_all(consult.select())

    @staticmethod
    async def search_consult(ticket, user):
        return await database.fetch_all(consult.select(consult.c.ticket == ticket).where(consult.c.user_id == user['id']))


    @staticmethod
    async def change_status(status: State, consult_id):
        await database.execute(consult.update(consult.c.id == consult_id).values(state=status))
