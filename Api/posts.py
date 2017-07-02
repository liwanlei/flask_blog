# -*- coding: utf-8 -*-
# @Date    : 2017-07-01 21:47:01
# @Author  : lileilei
from flask import jsonify,abort,make_response,request
from . import api
from app.models import Post,User
from app import db
@api.route('/get_post/<int:id>',methods=['GET'])
def get_posts(id):
    posts=Post.query.filter_by(id=id).first()
    if posts is None:
        abort(404)
    return jsonify([{
        'code':200,
        'post_title': posts.title,
        'post_udesc': posts.text,
        'post_comments':posts.comments.count(),
        'post_datetime':posts.publish_date,
        }])
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
    return jsonify([{'code':200, 'username': user.username,
    'regist_date':user.user_regest_date }])
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'没有找到你想要的需求'}), 404)