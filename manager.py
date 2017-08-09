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
from app.views import HomeView,RegView,LoginView,LogoutView,PersonFenleiView,TagViews,SerchView,NewView,PersonView,EditpersonView,PostViews,Userviews,RecommentView,EditpostView,FenleiHome
from Api import api
flask_admin = Admin(app,name=u'后台管理系统',index_view=AdminIndexView(
        name='导航栏',url='/wodeguanliyuan'))
flask_admin.add_view(UserView(db.session,name='用户'))
flask_admin.add_view(LinkView(db.session, name='链接'))
flask_admin.add_view(CommentView(db.session,name='评论'))
flask_admin.add_view(PostView(db.session,name='文章'))
flask_admin.add_view(TagView(db.session,name='标签'))
flask_admin.add_view(ClassView(db.session,name='分类'))
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
app.register_blueprint(api,url_prefix='/api')
app.add_url_rule('/',view_func=HomeView.as_view('home2'))
app.add_url_rule('/<int:page>',view_func=HomeView.as_view('home'))
app.add_url_rule('/reg',view_func=RegView.as_view('reg'))
app.add_url_rule('/login',view_func=LoginView.as_view('login'))
app.add_url_rule('/logout',view_func=LogoutView.as_view('logout'))
app.add_url_rule('/serch',view_func=SerchView.as_view('serch'))
app.add_url_rule('/new_post',view_func=NewView.as_view('new_post'))
app.add_url_rule('/center_person',view_func=PersonView.as_view('center_person'))
app.add_url_rule('/editperson',view_func=EditpersonView.as_view('editperson'))
app.add_url_rule('/post/<post_id>',view_func=PostViews.as_view('post'))
app.add_url_rule('/user/uername',view_func=Userviews.as_view('user'))
app.add_url_rule('/re_comment/<int:post_id>&<int:comment_id>&<string:user_id>',view_func=RecommentView.as_view('re_comment'))
app.add_url_rule('/editperson',view_func=EditpostView.as_view('edit'))
app.add_url_rule('/tag/<string:tag>&<int:page>',view_func=TagViews.as_view('tag'))
app.add_url_rule('/person/<string:fenlei1>',view_func=PersonFenleiView.as_view('peir'))
app.add_url_rule('/fenlei/<string:fenlei_name>&<int:page>',view_func=FenleiHome.as_view('fenlei'))
if __name__ == '__main__':
	manager.run()