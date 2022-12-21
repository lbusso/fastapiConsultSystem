import databases
import sqlalchemy
from decouple import config


DATABASE_URL = f"postgres://{config('DATABASE_USER')}:{config('DATABASE_PASSWORD')}@{config('DATABASE_HOST')}:{config('DATABASE_PORT')}/{config('DATABASE_NAME')}"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

