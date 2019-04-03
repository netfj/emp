
import sys
from os import path
dir = path.dirname(path.dirname(__file__))
sys.path.append(dir)


from setup_database import app,Person
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


d = {'resume_time': '2004.04-2009.10  杭州市余杭区城市管理综合行政执法大队 科员\n                  （2005.08-2007.12中共中央党校函授学院本科班公共管理专业在职学习）\n                  （2009年2月起参照公务员法管理）\n2009.10-2012.12  杭州市余杭区城市管政执法\n2012.12-2014.07  杭州市余杭区城市管理局城市管理科综合行政', 'resume_post': ''}

print(d)

try:
    re = Person.query.filter(Person.id==63).update(d)
    db.session.commit()
except Exception as e:
    print(e)