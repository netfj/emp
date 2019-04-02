#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   03.py 
time:   2019/4/2.19:28
"""


def main():
    pass


if __name__ == "__main__":
    main()


'''
session.execute(User.__table__.insert(),[{'name': `randint(1, 100)`,'age': randint(1, 100)} for i in xrange(10000)])
session.commit()

'''

from random import randint
a = [{'name': randint(1, 100),'age': randint(1, 100)} for i in range(10)]

print(a)