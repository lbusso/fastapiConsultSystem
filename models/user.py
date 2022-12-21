import sqlalchemy
from db import metadata
from models.enums import RoleType

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String(150), unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(120),),
    sqlalchemy.Column('first_name', sqlalchemy.String(120),),
    sqlalchemy.Column('last_name', sqlalchemy.String(120)),
    sqlalchemy.Column('phone', sqlalchemy.String(120)),
    sqlalchemy.Column('role', sqlalchemy.Enum(RoleType), nullable=True, server_default=RoleType.student.name),

)