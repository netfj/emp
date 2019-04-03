#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   09.py 
time:   2019/4/3.21:18
"""


#coding:utf-8
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:root@localhost/test',echo=True)

# 创建 ORM 基类
Base = declarative_base()
# 定义表
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

DB = sessionmaker(bind=engine)
session = DB()

session.query(User).filter(User.id > 2).update({"name" : "09"})

session.query(User).filter(User.id == 1).update({"name" : "10009"})

session.query(User).filter(User.id > 3).update({User.name: User.name + "11"}, synchronize_session=False)
session.query(User).filter(User.id > 4).update({"id": User.id + 10}, synchronize_session="evaluate")
session.commit()

r = session.query(User).filter(User.id<3).all()
for i in r:
    print(i.id,i.name)
