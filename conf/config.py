# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 20:17:16
# @Author  : lileilei
import os
class devconfig:
    SECRET_KEY = 'BaSeQuie'
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CSRF_ENABLED = True
    DEBUG = True
    UPLOAD_FOLDER='../app/static/acatar/'
    @staticmethod
    def init_app(app):
        pass
class testconfig:
    SECRET_KEY = 'BaSeQuie'
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CSRF_ENABLED = True
    DEBUG = True
    UPLOAD_FOLDER='../app/static/acatar/'
    @staticmethod
    def init_app(app):
        pass
class ProductionConfig:
    SECRET_KEY = 'BaSeQuie'
    basedir=os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "Production.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    UPLOAD_FOLDER='../app/static/acatar/'
    CSRF_ENABLED = True
    DEBUG = True
    @staticmethod
    def init_app(app):
        pass