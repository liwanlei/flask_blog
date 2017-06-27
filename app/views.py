# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 21:52
# @Author  : lileilei
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from app import app,db
from flask import render_template,redirect,flash,url_for,session,request
from app.models import Post,Tag,User,Link,Comment,Classifa
from app.form_app import Baselogin,Basereg,CommentFrom,PostForm
import datetime
def get_tui_link():
  link=db.session.query(Link).all()
  fenlei=db.session.query(Classifa).all()
  tuijian_post=Post.query.filter_by(is_recomment=True).all()
  return link,tuijian_post,fenlei
@app.route('/',methods=['GET'])
@app.route('/<int:page>')
def home(page=1):
	pagination=Post.query.order_by(Post.publish_date.desc()).paginate(page, per_page=10,error_out=False)
	posts = pagination.items
	link,tuijian_post,fenlei=get_tui_link()
	return render_template('home1.html',
                           posts=posts,
                           pagination=pagination,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/login',methods=['GET','POST'])
def login():
	form=Baselogin()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.username.data).first()
		check=user.check_password(form.password.data)
		if check==True:
			session['username']=form.username.data
			return redirect(url_for('home'))
		return render_template('login.html',form=form)
	return render_template('login.html',form=form)
@app.route('/reg',methods=['GET','POST'])
def reg():
	form=Basereg()
	if form.validate_on_submit():
		user=form.username.data
		user_reg=User.query.filter_by(username=user).first()
		if user_reg:
			return render_template('reg.html',form=form)
		else:
			if form.queren_pass.data != form.password.data:
				flash(message='两个密码输入是否一致')
				return render_template('reg.html',form=form)
			else:
				try:
					password=form.password.data
					add_user=User(username=user,
					user_regest_date=datetime.datetime.now())
					add_user.set_password(password=password)
					db.session.add(add_user)
					db.session.commit()
					return redirect(url_for('login'))
				except:
					return render_template('reg.html',form=form)
	return render_template('reg.html',form=form)
@app.route('/post/<string:post_id>',methods=['GET','POST'])
def post(post_id):
  post=Post.query.filter_by(id=post_id).first()
  user=User.query.filter_by(id=Post.user_id).first()
  link,tuijian_post,fenlei=get_tui_link()
  comment=Comment.query.filter_by(post_id=post.id).all()
  form=CommentFrom()
  if form.validate_on_submit:
    user_comment=session['username']
    user_id=User.query.filter_by(username=user_comment).first().id
    comment_ip=request.remote_addr
    text_comment=form.text.data
    date_now=datetime.datetime.now()
    add_comment=Comment(date=date_now,post_id=post_id,user_id=user_id,text=text_comment)
    db.session.add(add_comment)
    db.session.commit()
    return render_template('post.html',post=post,user=user,form=form,link=link,comments=reversed(comment),tuijian_post=tuijian_post)
  return render_template('post.html',post=post,user=user,
    form=form,link=link,comments=reversed(comment),tuijian_post=tuijian_post)
@app.route('/logout',methods=['GET','POST'])
def logout():
	session.clear()
	return redirect(url_for('home'))
@app.route('/python',methods=['GET'])
@app.route('/python/<int:page>')
def python1(page=1):
  pyth=Classifa.query.filter_by(name='python').first()
  pyth_post=pyth.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=pyth_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/java',methods=['GET'])
@app.route('/java/<int:page>')
def java1(page=1):
  java=Classifa.query.filter_by(name='java').first()
  java_post=java.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=java_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/appium',methods=['GET'])
@app.route('/appium/<int:page>')
def appium1(page=1):
  appium=Classifa.query.filter_by(name='appium').first()
  appium_post=appium.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=appium_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/selenium',methods=['GET'])
@app.route('/selenium/<int:page>')
def selenium1(page=1):
  selenium=Classifa.query.filter_by(name='selenium').first()
  selenium_post=selenium.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=selenium_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/interface',methods=['GET'])
@app.route('/interface/<int:page>')
def interface1(page=1):
  interface=Classifa.query.filter_by(name='接口').first()
  interface_post=interface.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=interface_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/jenkins',methods=['GET'])
@app.route('/jenkins/<int:page>')
def jenkins1(page=1):
  jenkins=Classifa.query.filter_by(name='Jenkins').first()
  jenkins_post=jenkins.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=jenkins_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/data',methods=['GET'])
@app.route('/data/<int:page>')
def data1(page=1):
  data=Classifa.query.filter_by(name='数据库').first()
  data_post=data.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=data_post,
                           tuijian_post=tuijian_post,fenleis=fenlei,                
                           links=link)
@app.route('/new_post',methods=['GET','POST'])
def new_post():
  if not session.get('username'):
    return  redirect(url_for('login'))
  tags=db.session.query(Tag).all()
  fenlei=db.session.query(Classifa).all()
  form = PostForm()
  if form.validate_on_submit():
      if request.form.get("checkbox") == None:
        is_recomment=False
      else:
        is_recomment=True
      new_post=Post(title=form.title.data,text=form.text.data,publish_date=datetime.datetime.now(),is_recomment=is_recomment)
      fenlei1=request.form.get('optionsRadios')
      classnmae=Classifa.query.filter_by(name=fenlei1).all()
      user_id=User.query.filter_by(username=session['username']).first()
      tag_s=request.form.getlist('tag')
      newpost_tag=[]
      for tag in tag_s:
        new_tag=Tag.query.filter_by(name=tag).first()
        newpost_tag.append(new_tag)
      new_post.tag=newpost_tag
      new_post.classname=classnmae
      db.session.add(new_post)
      db.session.commit()
      return  redirect(url_for('home'))
  return render_template('newpost.html',tags=tags,fenleis=fenlei,form=form)

@app.route('/person',methods=['GET','POST'])
def center_person():
  if not session.get('username'):
    return redirect(url_for('login'))
  user_id=User.query.filter_by(username=session.get('usernmae')).first()
  posts=Post.query.filter_by(user_id=user_id).all()
  tuijian_posts = Post.query.filter_by(user_id=user_id,is_recomment=True).all()
  pingluns=Post.query.filter_by(user_id=user_id).first()
  return render_template('person_center.html',posts=posts,tuijian_posts=tuijian_posts)