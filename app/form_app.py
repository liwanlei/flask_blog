# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 11:37:06
# @Author  : lileilei
from flask_wtf import Form
from wtforms import PasswordField,StringField,TextAreaField,IntegerField,SubmitField,validators,DateTimeField,BooleanField,SelectMultipleField,FileField
from wtforms.validators import DataRequired
from app.models import User
class Baselogin(Form):
	username=StringField('用户名',[validators.length(min=6, max=16,message='用户名长度6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入用户名'})
	password=PasswordField('密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
	def validate(self):
		check_validata=super(Baselogin,self).validate()
		if not check_validata:
			return False
		else:
			user=User.query.filter_by(username=self.username.data).first()
			if not user:
				self.username.errors.append('用户名不存在')
				return False
			if not user.check_password(self.password.data):
				self.username.errors.append('密码不正确')
				return False
			return True
class Basereg(Form):
	username=StringField('用户名',[validators.length(min=6, max=16,message='用户名长度6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入用户名'})
	password=PasswordField('密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
	queren_pass=PasswordField('确认密码',[validators.length(min=6, max=16,message='密码长度是6-16'),validators.DataRequired()],render_kw={'placeholder':u'输入密码'})
	def  validate(self):
		check_validate = super(Basereg, self).validate()
		if not check_validate:
			return False
		user=User.query.filter_by(username=self.username.data).first()
		if user:
			self.username.errors.append('用户名已经存在')
			return False
		return True
class find_pass(Form):
	email = StringField('email', [validators.DataRequired()],render_kw={'placeholder':u'请输入邮箱'})
class PostForm(Form):
	title = StringField('标题',validators=[validators.DataRequired(),validators.length(min=1,max=255,message='请输入评论内容')],render_kw={'placeholder':u'请输入标题'})
	text = TextAreaField('正文',validators= [validators.DataRequired()])
class CommentFrom(Form):
	text=TextAreaField(u'评论',validators=[validators.length(min=1,message='请输入评论内容'),validators.DataRequired()],render_kw={'placeholder':u'请输入评论内容'})
class EditPersonFrom(Form):
	name=StringField('用户昵称',[validators.length(min=6, max=16,message='用户昵称有误'),validators.DataRequired()],render_kw={'placeholder':u'用户昵称'})
	qq=IntegerField('qq',[validators.DataRequired()])
	user_email=StringField('邮箱',[validators.length(min=4,max=20,message='邮箱错误'),validators.DataRequired()])
	avatar=FileField('头像')
	submit=SubmitField('保存修改')