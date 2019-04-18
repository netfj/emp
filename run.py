#coding:utf-8
# @Info:
# @Author:Netfj@sina.com @File:run.py @Time:2019/4/18 14:24

import logging
from flask import render_template,flash,request,redirect,url_for
from setup_database import app, Person, Record_info, Home, Dwdm

import surport
surport.logset()

logging.info('test')

@app.route('/')
def hello_world():
    dwdm = Dwdm.query.all()
    for x in dwdm:
        print(x.id,x.dm,x.mc)
    return render_template('main_query.html',dwdm = dwdm)

if __name__ == '__main__':
    app.run()

