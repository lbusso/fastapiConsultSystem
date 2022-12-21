from db import database
from models.consult import reply, consult
from models.user import user
from models.enums import State
from services.ses import SESServices

ses = SESServices()

class ReplyManager:
    @staticmethod
    async def create_reply(reply_data, consult_id):
        reply_data['consult_id'] = consult_id
        consult_ = await database.fetch_one(consult.select(consult.c.id == consult_id))
        user_ = await database.fetch_one(user.select(user.c.id == consult_.user_id))
        id_ = await database.execute(reply.insert().values(reply_data))

        ses.send_mail("Your consult has been answered ", [user_.email], reply_data['text'])

        return await database.fetch_one(reply.select(reply.c.id == id_))

    @staticmethod
    async def get_reply(consult_id):
        return await database.fetch_all(reply.select(reply.c.consult_id == consult_id))