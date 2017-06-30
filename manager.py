# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 08:43:19
# @Author  : lileilei
from flask_script import Manager,Server
from  app import app,db
from  datetime import  timedelta
from flask_admin import Admin,AdminIndexView
from common.admin_view import UserView,LinkView,CommentView,PostView,TagView,ClassView
from flask_admin.contrib.sqla import  ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_moment import Moment
flask_admin = Admin(app,name=u'后台管理系统',index_view=AdminIndexView(
        name='导航栏',
        url='/wodeguanliyuan'
    ))
flask_admin.add_view(UserView(db.session,name='用户'))
flask_admin.add_view(LinkView(db.session, name='链接'))
flask_admin.add_view(CommentView(db.session,name='评论'))
flask_admin.add_view(PostView(db.session,name='文章'))
flask_admin.add_view(TagView(db.session,name='标签'))
flask_admin.add_view(ClassView(db.session,name='分类'))
manager=Manager(app)
moment=Moment(app)
manager.add_command('run',Server(use_debugger=True))
app.permanent_session_lifetime=timedelta(minutes=50)
if __name__ == '__main__':
	manager.run()