#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   04.py 
time:   2019/4/2.19:44
"""

import MySQLdb
def dic2sql(dic, sql):
    sf = ''
    for key in dic:
        tup = (key, dic[key])
        sf += (str(tup) + ',')
        sf = sf.rstrip(',')
        sql2 = sql % sf
        return sql2

if __name__ == '__main__':
    dic = {'apple': 216, 'jar': 138}
    sql = "insert into users (login,userid) VALUES %s;"
    ret = dic2sql(dic, sql)
    # print(ret) # 连接MySQL，并提交数据
    cxn = MySQLdb.connect(user='root',password='password', db='test')
    cur = cxn.cursor()
    cur.execute(ret)
    cxn.commit()
    cxn.close()
