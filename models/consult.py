import sqlalchemy
from db import database, metadata
from models.enums import State, Category
from datetime import datetime


consult = sqlalchemy.Table(
    'consults',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('ticket', sqlalchemy.String(11), unique=True, nullable=False),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id'), nullable=False),
    sqlalchemy.Column('category', sqlalchemy.Enum(Category), nullable=False),
    sqlalchemy.Column('text', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('state', sqlalchemy.Enum(State), server_default=State.pending.name),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),

)

reply = sqlalchemy.Table(
    'replys',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('consult_id', sqlalchemy.ForeignKey('consults.id'), nullable=False),
    sqlalchemy.Column('text', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, server_default=sqlalchemy.func.now())
)
