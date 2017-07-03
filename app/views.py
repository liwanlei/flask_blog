# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 21:52
# @Author  : lileilei
# @Site    : 
# @File    : views.py
# @Software: PyCharm
from app import app,db
from flask_login import login_required,login_user
from flask import render_template,redirect,flash,url_for,session,request
from app.models import Post,Tag,User,Link,Comment,Classifa
from conf.loadconfig import lod_config
from app.form_app import Baselogin,Basereg,CommentFrom,PostForm,EditPersonFrom
import datetime,os
from common.yanzhengma import generate_verification_code
from common.fenye import list_qiepian
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
	return render_template('home1.html',posts=posts,pagination=pagination,
    tuijian_post=tuijian_post,fenleis=fenlei,                
    links=link)
@app.route('/login',methods=['GET','POST'])
def login():
	form=Baselogin()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.username.data).first()
		check=user.check_password(form.password.data)
		if check==True:
			login_user(user)
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
					add_user=User(username=user,name=user,
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
  fenleis=db.session.query(Classifa).all()
  post=Post.query.filter_by(id=post_id).first()
  user=User.query.filter_by(id=Post.user_id).first()
  link,tuijian_post,fenlei=get_tui_link()
  comment=Comment.query.filter_by(post_id=post.id).all()
  form=CommentFrom()
  if form.validate_on_submit():
    user_comment=session['username']
    user_id=User.query.filter_by(username=user_comment).first().id
    comment_ip=request.remote_addr
    if form.text.data is None:
      return render_template('post.html',fenleis=fenleis,post=post,user=user,form=form,link=link,comments=reversed(comment),tuijian_post=tuijian_post)
    text_comment=form.text.data
    date_now=datetime.datetime.now()
    add_comment=Comment(date=date_now,post_id=post_id,user_id=user_id,text=text_comment)
    db.session.add(add_comment)
    db.session.commit()
    return render_template('post.html',fenleis=fenleis,post=post,user=user,form=form,link=link,comments=reversed(comment),tuijian_post=tuijian_post)
  return render_template('post.html',post=post,user=user,fenleis=fenleis,
    form=form,link=link,comments=reversed(comment),tuijian_post=tuijian_post)
@app.route('/logout',methods=['GET','POST'])
def logout():
	session.clear()
	return redirect(url_for('home'))
@app.route('/fenlei/<string:fenlei_name>')
@app.route('/fenlei/<string:fenlei_name>&<int:page>')
def fenlei(fenlei_name,page=1):
  pyth=Classifa.query.filter_by(name=fenlei_name).first()
  pyth_post=pyth.posts
  page1=list_qiepian(pyth_post,10)
  pages=range(1,len(page1)+1)
  pyth_post1=page1[int(page)-1]
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',posts=pyth_post1,pages=pages,tuijian_post=tuijian_post,fenleis=fenlei,links=link)
@app.route('/new_post',methods=['GET','POST'])
@login_required
def new_post():
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
      user_id=User.query.filter_by(username=session['username']).first().id
      tag_s=request.form.getlist('tag')
      newpost_tag=[]
      for tag in tag_s:
        new_tag=Tag.query.filter_by(name=tag).first()
        newpost_tag.append(new_tag)
      new_post.user_id=user_id
      new_post.tag=newpost_tag
      new_post.classname=classnmae
      db.session.add(new_post)
      db.session.commit()
      return  redirect(url_for('home'))
  return render_template('newpost.html',tags=tags,fenleis=fenlei,form=form)
@app.route('/person',methods=['GET','POST'])
@login_required
def center_person():
  user_id=User.query.filter_by(username=session.get('username')).first()
  posts=Post.query.filter_by(user_id=user_id.id).all()
  tuijian_posts = Post.query.filter_by(user_id=user_id.id,is_recomment=True).all()
  tag_in=[]
  for post in posts:
    tag_in.append(post.classname[0])
  fenleis=set(tag_in)
  return render_template('person_center.html',username=user_id,posts=posts,tuijian_posts=tuijian_posts,fenleis=fenleis)
@app.route('/person/<string:fenlei1>',methods=['GET','POST'])
@login_required
def person(fenlei1):
  user_id=User.query.filter_by(username=session.get('usernmae')).first()
  post_fenlei=Post.query.filter_by(user_id=user_id).all()
  classnmae=Classifa.query.filter_by(name=fenlei1).all()
  tuijian_posts = Post.query.filter_by(user_id=user_id,is_recomment=True).all()
  tag_in=[]
  posts=Post.query.filter_by(user_id=user_id).all()
  for post in posts:
    tag_in.append(post.classname[0])
  fenleis=set(tag_in)
  fenlei_list=[]
  for i in post_fenlei:
    if i.classname==classnmae:
      fenlei_list.append(i)
    else:
      continue
  return render_template('gerenfenlei.html',fenlei_lists=fenlei_list,tuijian_posts=tuijian_posts,
    fenleis=fenleis)
@app.route('/tag/<string:tag>',methods=['GET','POST'])
@app.route('/tag/<string:tag>&<int:page>')
def tag(tag,page=1):
  tags=Tag.query.filter_by(name=tag).first()
  posts=tags.posts
  link,tuijian_post,fenlei=get_tui_link()
  return render_template('home.html',
                           posts=posts,
                           tuijian_post=tuijian_post,fenleis=fenlei,
                           links=link)
@app.route('/edit/<string:post_id>',methods=['GET',"POST"])
@login_required
def edit(post_id):
    post=Post.query.filter_by(id=post_id).first()
    form=PostForm()
    tags = db.session.query(Tag).all()
    fenleis = db.session.query(Classifa).all()
    post_user=User.query.filter_by(id=post.user_id).first().username
    if session['username']!=post_user:
        return  redirect(url_for('center_person'))
    if form.validate_on_submit():
        if request.form.get("checkbox") == None:
            is_recomment = False
        else:
            is_recomment = True
        post.is_recomment=is_recomment
        fenlei1 = request.form.get('optionsRadios')
        classnmae = Classifa.query.filter_by(name=fenlei1).all()
        user_id = User.query.filter_by(username=session['username']).first().id
        tag_s = request.form.getlist('tag')
        newpost_tag = []
        for tag in tag_s:
            new_tag = Tag.query.filter_by(name=tag).first()
            newpost_tag.append(new_tag)
        post.tag = newpost_tag
        post.classname = classnmae
        post.title = form.title.data
        post.text = form.text.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post',post_id=post_id))
    form=PostForm()
    form.title.data=post.title
    form.text.data=post.text
    return render_template('edit.html',form=form,tags=tags,fenleis=fenleis)
@app.route('/user/<string:username>',methods=['GET','POST'])
def user(username):
  if session.get('username'):
    if username==session['username']:
      return redirect(url_for('center_person'))
    user_id=User.query.filter_by(username=username).first()
    posts=Post.query.filter_by(user_id=user_id).all()
    tuijian_posts = Post.query.filter_by(user_id=user_id,is_recomment=True).all()
    return render_template('user.html',username=username,posts=posts,tuijian_posts=tuijian_posts)
  user_id=User.query.filter_by(username=username).first().id
  posts=Post.query.filter_by(user_id=user_id).all()
  tuijian_posts = Post.query.filter_by(user_id=user_id,is_recomment=True).all()
  return render_template('user.html',username=username,posts=posts,tuijian_posts=tuijian_posts)
@app.route('/editperson',methods=['GET','POST'])
@login_required
def editperson():#这里目前需要对上传路径进行优化
  user=User.query.filter_by(username=session['username']).first()
  form=EditPersonFrom()
  if form.validate_on_submit():
    user.name=form.name.data
    user.user_email=form.user_email.data
    user.user_qq=form.qq.data
    avatar=request.files['avatar']
    fanme=avatar.filename
    upfile=os.getcwd()+('/app/static/avatar/')
    ALLOWER_EXIT=['pang','jpg','jpeg','jig']
    flag='.' in fanme and fanme.split('.')[1] in ALLOWER_EXIT
    if not flag:
      return render_template('editperson.html',form=form)
    avatar.save('{}{}{}'.format(upfile,user.username,fanme))
    user.user_image='/static/avatar/{}{}'.format(user.username,fanme)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('center_person'))
  form.qq.data=user.user_qq
  form.user_email.data=user.user_email
  form.name.data=user.name
  return render_template('editperson.html',form=form)
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'),404
@app.errorhandler(505)
def page_not_found(e):
  return render_template('505.html'),505
