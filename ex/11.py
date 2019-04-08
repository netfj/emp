#coding:utf-8
# @Info:   从 WORD DOCX 文件中提取图片
# @Author: Netfj@sina.com @File:05.py @Time:2019/3/29 15:08

from os.path import basename
import docx


open_word_file = r'd:\temp\emp_sample.docx'
try:
    doc = docx.Document(open_word_file)  # 打开文件
except Exception as e:
    msg = '打开文件({})错误：{}'.format(open_word_file, e)
    print(msg)
else:
    msg = '打开文件成功!'
    print(msg)

for shape in doc.inline_shapes:
    contentID = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
    contentType = doc.part.related_parts[contentID].content_type
    if not contentType.startswith('image'):
        continue
    imgData = doc.part.related_parts[contentID]._blob



import sys
from os import path
dir = path.dirname(path.dirname(__file__))
sys.path.append(dir)
from setup_database import app,Person
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

p = Person()
p.name = 'test'
p.photo = imgData
db.session.add(p)
db.session.commit()

item = db.session.query(Person).filter(Person.id==11)
for x in item:
    # print(x.id,x.name,x.photo)
    with open('test01.jpeg', 'wb') as fp:
        fp.write(x.photo)