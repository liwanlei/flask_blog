# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 20:22:48
# @Author  : lileilei
from app import db,app
import datetime
from werkzeug.security import check_password_hash,generate_password_hash
posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.Integer(), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer(), db.ForeignKey('tags.id')))
followers = db.Table('followers',
    db.Column('follower_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('followed_id', db.Integer(), db.ForeignKey('users.id')))
post_class=db.Table('post_class',
    db.Column('post_id',db.Integer(),db.ForeignKey('posts.id')),
    db.Column('classifa_id',db.Integer(),db.ForeignKey('fenlei.id')))
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    username=db.Column(db.String(64),unique=True,index=True)
    name=db.Column(db.String(64),default=username,nullable=True)
    password=db.Column(db.String(64),unique=True)
    user_regest_date = db.Column(db.DateTime(), default=datetime.datetime.now())
    user_email=db.Column(db.String(64),nullable=True)
    user_qq=db.Column(db.Integer(),nullable=True,unique=True)
    last_time_login=db.Column(db.DateTime(),default=datetime.datetime.now())
    user_image=db.Column(db.String(252),nullable=True)
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')
    followed = db.relationship('User',
                               secondary=followers,
                               primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')
    comment = db.relationship(
        'Comment',
        backref='users',
        lazy='dynamic')
    def __repr__(self):
        return  self.username
    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
        return  check_password_hash(self.password,password=password)
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self
    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0
    def followed_posts(self):
        return  Post.query.join(followers,((followers.c.followed_id == Post.user_id).filter(followers.c.follower_id == self.id).order_by(Post.timestamp.desc())))
    def is_authenticated(self):
        return True
    def is_active(self): 
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    title=db.Column(db.String(255),unique=False)
    text=db.Column(db.Text())
    publish_date=db.Column(db.DateTime(),default=datetime.datetime.now())
    user_id=db.Column(db.Integer(),db.ForeignKey('users.id'))
    is_recomment=db.Column(db.Boolean(),default=False)
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    tag = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )
    classname=db.relationship('Classifa',
    	secondary=post_class,
    	backref=db.backref('posts'))
    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(),default=datetime.datetime.now())
    post_id =db.Column(db.Integer(), db.ForeignKey('posts.id'))
    user_id=db.Column(db.Integer(),db.ForeignKey('users.id'))
    pid=db.Column(db.Integer(),db.ForeignKey('comments.id'))
    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.text)
comment=db.relationship('Comment',backref='comment_id',lazy='dynamic', uselist=False)
class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(255))
    def __repr__(self):
        return self.name
class Link(db.Model):
    __tablename__='links'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    def __repr__(self):
        return  '<User %r>' % self.name
class Classifa(db.Model):
    __tablename__='fenlei'
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(64))
    def __repr__(self):
        return self.name