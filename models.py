from peewee import *




db = PostgresqlDatabase('dry', 'dry')


class BaseModel(Model):
    class Meta:
        database = db


class FlaskDojo(BaseModel):
    request_counter = IntegerField()

