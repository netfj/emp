#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   03.py 
time:   2019/4/2.19:28
"""
from random import randint
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'mysql+mysqldb://root:root@localhost/employee?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(30))
    age  = Column(String(60))

drop_db()
init_db()

BaseModel = declarative_base()
session.execute(User.__table__.insert(),
                [{'name': randint(1, 100),'age': randint(1, 100)} for i in range(40)])
session.commit()

session.execute(User.__table__.insert(),
                [
                    {'name': "测试",'age': '以字典形式加入记录'},
                    {'name': '姓名','age': 99}
                ])
session.commit()
