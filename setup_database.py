#coding:utf-8
# @Info: 建立人员档案的数据库模型
# @Author:Netfj@sina.com @File:20_emp_database.py @Time:2019/3/30 18:37

from sqlalchemy import create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化：创建数据库
def create_data(database_name = None):
    engine = create_engine('mysql+mysqldb://root:root@localhost',
                           encoding = "utf-8", echo = True, max_overflow = 5)
    #创建数据库
    cur = engine.execute('show databases')
    f = cur.fetchall()
    if (database_name,) not in f:
        try:
            engine.execute('create database ' + database_name)
        except Exception as e:
            return ("Error: ",e)
        else:
            return ("数据库创建成功")
    else:
        return ('数据库已经存在')
re = create_data('employee')

# 建立表的模型
app = Flask(__name__)
# 数据库引擎
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:root@localhost/employee'

# 请求结束后自动commit(但操作数据库除外，需要 commit)
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# 显示执行的SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 跟踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化连接
db = SQLAlchemy(app)

# 定义表的模型
class Person(db.Model):
    __tablename__ = "persons"
    id          = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_department = db.Column(db.Integer)
    name        = db.Column(db.String(64))
    birthday    = db.Column(db.String(30))
    D_birthday  = db.Column(db.Date())
    nation      = db.Column(db.String(36))
    native      = db.Column(db.String(36))
    birthplace  = db.Column(db.String(36))
    party_time  = db.Column(db.String(30))
    D_party_time= db.Column(db.Date())
    work_time   = db.Column(db.String(30))
    D_work_time = db.Column(db.Date())
    health      = db.Column(db.String(36))
    profession  = db.Column(db.String(60))
    speciality  = db.Column(db.String(60))
    education1  = db.Column(db.String(60))
    academy1    = db.Column(db.String(60))
    education2  = db.Column(db.String(60))
    academy2    = db.Column(db.String(60))
    post_now    = db.Column(db.String(100))
    post_will   = db.Column(db.String(100))
    post_remove = db.Column(db.String(100))
    resume_time = db.Column(db.String(36))
    resume_post = db.Column(db.String(100))

    '''
        'name':'姓名', 'gender':'性别', 'birthday':'出生年月',
        'nation':'民族', 'native':'籍贯','birthplace':'出生地',
        'party_time':'入党时间', 'work_time':'参加工作时间','health':'健康状况',
        'profession':'专业技术职务','speciality':'熟悉专业有何专长',
        'education1':'全日制教育', 'academy1':'毕业院校系及专业',
        'education2':'在职教育', 'academy2':'毕业院校系及专业',
        'post_now':'现任职务',
        'post_will':'拟任职务',
        'post_remove':'拟免职务',
        'resume_time':'简历时间','resume_post':'简历岗位'
    '''

    def __repr__(self):
        return '<Person:{}.{}>'.format(self.id,self.name)

if __name__ == '__main__':
    # 删除所有表（注意要终止以前开设的进程）
    db.drop_all()

    # 创建表（前面定义的模型）
    db.create_all()
