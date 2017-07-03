# -*- coding: utf-8 -*-
# @Date    : 2017-07-03 20:41:52
# @Author  : lileilei
from app.models import db,User,Post,Tag,Classifa
import random,datetime
user=db.session.query(User).first()
# print(user.id)
# tag_list=['python','selenium','接口','Jenkins','appium','java','数据库','python_selenium','python_appium','java_selenium','java_appium','集成','测试框架']
# for i in tag_list:
#     tag=Tag(name=i)
#     db.session.add(tag)
#     db.session.commit()
# clasname=['python','selenium','接口','Jenkins','appium','java','数据库']
# for i in clasname:
#     new_class=Classifa(name=i)
#     db.session.add(new_class)
#     db.session.commit()
# user = db.session.query(User).first()
# tag_one = Tag(name='python')
# tag_two = Tag( name='selenium')
# tag_three = Tag( name='接口')
# tag_four = Tag( name='Jenkins')
# class_one=Classifa(name='python')
# class_two=Classifa(name='selenium')
# class_three=Classifa(name='接口')
# class_four=Classifa(name='Jenkins')
# class_five=Classifa(name='appium')
# class_six=Classifa(name='java')
# class_se=Classifa(name='数据库')
# tag_list = [tag_one, tag_two, tag_three, tag_four]
# class_list=[class_one,class_two,class_three,class_four,class_five,class_six,class_se]
# s = "EXAMPLE TEXT"
# for i in range(1000):
#     new_post = Post( title="Post" + str(i))
#     new_post.publish_date = datetime.datetime.now()
#     new_post.text = s*100
#     new_post.tags = random.sample(tag_list, random.randint(1, 3))
#     new_post.classname=random.sample(class_list,random.randint(1,1))
#     db.session.add(new_post)
# db.session.commit()
