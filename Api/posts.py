# -*- coding: utf-8 -*-
# @Date    : 2017-07-01 21:47:01
# @Author  : lileilei
from flask import jsonify,abort,make_response
from . import api
from app.models import Post
from app import db
@api.route('/get_post/<int:id>',methods=['GET'])
def get_posts(id):
    posts=Post.query.filter_by(id=id).first()
    if posts is None:
        abort(404)
    return jsonify({
        'content-type': 'application/json',
        'code':200,
        'post_title': posts.title,
        'post_udesc': posts.text,
        'post_comments':posts.comments.count(),
        'post_datetime':posts.publish_date,
        })
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'没有找到你想要的需求'}), 404)