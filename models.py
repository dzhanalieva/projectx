from peewee import *
import datetime
from flask_login import UserMixin # UserMixin расширяет дочерний класс

db = PostgresqlDatabase(
    'flask_project',
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    password = '0709'
)

class BaseModel(Model):
    class Meta:
        database = db

class MyUser(UserMixin, BaseModel):
    email = CharField(max_length=225, null = False, unique = True)
    name = CharField(max_length=225, null = False )
    second_name = CharField(max_length=225, null = False )
    password = CharField(max_length=225, null = False )
    age = IntegerField()

    def __repr__(self):
        return self.email
 
class Post(BaseModel):
    author = ForeignKeyField(MyUser, on_delete ='CASCADE')
    title = CharField(max_length=225, null = False)
    description = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return self.title
    
db.create_tables([MyUser, Post])
