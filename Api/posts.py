# -*- coding: utf-8 -*-
# @Date    : 2017-07-01 21:47:01
# @Author  : lileilei
from flask import jsonify,abort,make_response,request
from . import api
from app.models import Post,User,Comment,Tag,Classifa
from app import db
@api.route('/get_post_one/<int:id>',methods=['GET'])
def get_post_one(id):
    post=Post.query.filter_by(id=id).first()
    if post is None:
        abort(404)
    return jsonify([{
        'code':200,
        'post':post.to_json()}])
@api.route('/api/regist',methods=['POST'])
def new_user():
    username=request.json.get('usernmae')
    password=request.json.gey('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # 
    user = User(username = username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify([{'code':200, 'username': user.username,'regist_date':user.user_regest_date }])
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'没有找到你想要的需求'}), 404)
@api.route('/get_comment_one/<int:id>',methods=['GET'])
def get_comment_one(id):
    comment=Comment.query.filter_by(id=id).first()
    if comment is None:
        abort(404)
    return jsonify([{'code':200,'comment':comment.to_json()}])
@api.route('/get_user_one/<string:username>',methods=['GET'])
def get_user_one(username):
    user=User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return jsonify([{'code':200,'user':user.to_json()}])
@api.route('/get_tag_post/<string:tagname>',methods=['GET'])
def get_tag_post(tagname):
    tag=Tag.query.filter_by(name=tagname).first()
    if tag is None:
        abort(404)
    tag_posts=tag.posts
    return jsonify([{'code':200,'tag_posts':[tag_post.to_json()for tag_post in tag_posts]}])
@api.route('/get_fenlei_post/<string:fenleiname>',methods=['GET'])
def get_fenlei_post(fenleiname):
    fenlei_post=Classifa.query.filter_by(name=tagname).first()
    if fenlei_post is None:
        abort(404)
    fenlei_posts=fenlei_post.posts
    return jsonify([{'code':200,'tag_posts':[fenlei_post.to_json()for fenlei_post in fenlei_posts]}])