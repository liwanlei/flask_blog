# encoding: utf-8
'''
@author: lileilei
@file: __init__.py
@time: 2017/5/6 10:33
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from  flask_sqlalchemy import SQLAlchemy
from  flask_mail import Mail
from conf import loadconfig
from  flask_cache import Cache
from flask_moment import  Moment
import os
from  datetime import  timedelta
os.environ['MODE']=''
app=Flask(__name__)
config = loadconfig.lod_config()
app.config.from_object(config)
db=SQLAlchemy(app)
cache=Cache(app)
moment=Moment(app)
bootstrp=Bootstrap(app)
mail=Mail(app)
app.permanent_session_lifetime=timedelta(minutes=50)
from  app import views,models,url
