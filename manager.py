# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 08:43:19
# @Author  : lileilei
from flask_script import Manager,Server
from  app import app,db
from app.models import User
from flask_login import LoginManager
from  datetime import  timedelta
from flask_admin import Admin,AdminIndexView
from common.admin_view import UserView,LinkView,CommentView,PostView,TagView,ClassView
from flask_admin.contrib.sqla import  ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_moment import Moment
manager=Manager(app)
moment=Moment(app)
loginManager=LoginManager(app)
loginManager.session_protection='strong'
loginManager.login_view='login'
loginManager.init_app(app)
@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
manager.add_command('run',Server(use_debugger=True))
app.permanent_session_lifetime=timedelta(minutes=50)
if __name__ == '__main__':
	app.run()
