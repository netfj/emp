#coding:utf-8
# @Info: 
# @Author:Netfj@sina.com @File:07.py @Time:2019/4/3 13:01

from flask_sqlalchemy import SQLAlchemy
from os import path
import sys
sys.path.append(path.dirname(path.dirname('__filename')))

from setup_database import app,Person

db  = SQLAlchemy(app)

re = db.session.execute(Person.__table__.insert(),
                   {'name':'zhangsan'})

re2 = db.session.commit()

# re3 = db.session.execute('select id,name from employee.persons').fetchall()
# print(re3)

print('==========')
re4 = db.session.query(Person).filter_by(id = 98)
for i in re4:
    print(i.id,i.name)

print('---------')

re5 = Person.query.filter(Person.id>88).all()   # 这是迭代器
for i in re5:
    print(i.id,i.name)


