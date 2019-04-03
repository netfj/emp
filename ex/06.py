#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库引擎
app.config["SQLALCHEMY_DATABASE_URI"]='mysql://root:root@localhost/test'

# 请求结束后自动commit(但操作数据库除外，需要 commit)
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# 显示执行的SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 跟踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化连接
db = SQLAlchemy(app)

# 定义表的模型
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role = db.Column(db.String(64))

    def __repr__(self):
        """非必须, 用于在调试或测试时, 返回一个具有可读性的字符串表示模型."""
        return '<User %r>' % self.username

# 删除所有表（注意要终止以前开设的进程）
db.drop_all()

# 创建表（前面定义的模型）
db.create_all()

# 增加记录：方式一（简捷）
db.session.add(Role(id='1',name='Role test1'))
db.session.add(User(id='1',username='User test1'))
db.session.commit()

# 增加记录：方式二（规范）
role = Role()
role.id = 2     # 对于数字型，可以以数字形式赋值
role.name = "role test2"
user = User()
user.id = "2"
user.username = "user test2"
db.session.add(role,user)
db.session.commit()

# 增加记录：方式三（批量：以列表形式加入）
admin_role = Role(name="Admin")
mod_role = Role(name="Moderator")
user_role = Role(name="User")
user_john = User(username="john", role=admin_role)
user_susan = User(username="susan", role=mod_role)
user_david = User(username="david", role=user_role)
db.session.add_all([admin_role, mod_role, user_role,
                    user_john, user_susan, user_david])
db.session.commit()

# 方法四：以字典形式
db.session.execute(User.__table__.insert(),[{'username':'张三','role':'角色1'},{'username':'李四','role':'角色2'}])
db.session.commit()

# 方法五：直接增加，这也是直接运行SQL的例子
sql = "insert into users (username, role) values ('abc','123'),('xyz','456')"
db.session.execute(sql)
db.session.commit()


# 测__repr__ 的返回值
print(admin_role)
print(user_john)

# 查询记录
u1 = User.query.all()   #全部记录
u2 = User.query.first() #首个记录
print(u1,'\n',u2)
for x in u1:
    print(x.id,x.username)

# 查询：筛选/按条件查询
r = Role.query.filter(Role.id<3).all()
print(r)

# 修改：方法一
r = Role.query.filter(Role.id==1)
r.update({'name':'New name 001'})
db.session.commit()

# 修改：方法二
Role.query.filter(Role.id==2).update({'name':'New name 002'})
db.session.commit()

# 删除记录
User.query.filter(User.id==1).delete()
db.session.commit()




#结束进程
import sys
sys.exit()
