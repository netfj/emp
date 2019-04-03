#coding:utf-8
# @Info:
# @Author:Netfj@sina.com @File:05.py @Time:2019/4/3 7:54

import sys
from os import path
dir = path.dirname(path.dirname(__file__))
sys.path.append(dir)


from setup_database import app,Person
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

db.session.execute('create table t1 (id Int);')
db.session.commit()