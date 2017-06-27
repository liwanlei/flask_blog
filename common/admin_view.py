# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: admin_view.py
@time: 2017/6/23 17:41
"""
from  flask_admin import  AdminIndexView,Admin,BaseView
from flask_admin.contrib.sqla import  ModelView
from  app.models import Tag,Post,Comment,User,Link,Classifa
class UserView(ModelView):
    can_create = True
    column_labels={
    'id':'序号',
    'username':'用户名',
    'password':'密码',
    'user_regest_date':'注册时间',
    'user_email':'用户邮箱',
    'user_qq':'用户QQ',
    'user_image':'头像',
    }
    column_list=['id','username','password','user_regest_date','user_email','user_qq','user_image']
    def __init__(self,session,**kwargs):
        super(UserView,self).__init__(User,session,**kwargs)
class PostView(ModelView):
	can_create=True
	column_labels={
    'id':'序号',
    'title':'标题',
    'text':'正文',
    'publish_date':'创建日期',
    'user_id':'创建用户id',
    'is_recomment':'是否推荐',
    'tag':'标签',
    'classname':'分类'}
	column_list=['id','title','text','publish_date','user_id','is_recomment','tag','classname']
	def __init__(self,session,**kwargs):
		super(PostView,self).__init__(Post,session,**kwargs)
class TagView(ModelView):
	can_create=True
	column_labels = {
        'id':u'序号',
        'name':'标签名字'
    }
	column_list=['id','name']
	def __init__(self,session,**kwargs):
		super(TagView,self).__init__(Tag,session,**kwargs)
class CommentView(ModelView):
	can_create=True
	column_labels={
        'id':'序号',
        'text':'评论内容',
        'date':'评论日期',
        'post_id':'文章id',
        'user_id':'用户id'
    }
	column_list=['id','text','date','post_id','user_id']
	def __init__(self,session,**kwargs):
		super(CommentView,self).__init__(Comment,session,**kwargs)
class LinkView(ModelView):
	can_create=True
	column_labels = {
        'id':u'序号',
        'name':'链接名字',
        'url':'链接地址',
    }
	column_list=['id','name','url']
	def __init__(self,session,**kwargs):
		super(LinkView,self).__init__(Link,session,**kwargs)
class ClassView(ModelView):
    can_create=True
    column_labels = {
        'id':u'序号',
        'name':'分类',
    }
    column_list=['id','name']
    def __init__(self,session,**kwargs):
        super(ClassView,self).__init__(Classifa,session,**kwargs)
