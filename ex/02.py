from setup_database import app,Record_info
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

record_info = Record_info()
record_info.id_person = 11
# record_info.mode = 'word'
# record_info.info = 'test'
# record_info.data_souce = self.table_info
# record_info.data_clean = self.table_info_clean
# record_info.data2db = self.data2db
# record_info.dt = datetime.today()


# print(record_info.id_person,
#       record_info.mode, record_info.info)

try:
    db.session.add(record_info)
    db.session.commit()
    print('sucess!')
except Exception as e:
    db.session.rollback()
    print('fail')

db.session.execute('CREATE TABLE studant (id INTEGER)')
db.session.commit

from random import randint
db.session.execute(User.__table__.insert(),
                   [{'name': randint(1, 100),'age': randint(1, 100)} for i in range(10000)])
db.session.commit()