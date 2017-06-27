# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 09:04:57
# @Author  : lileilei 
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app import db,app
migrete=Migrate(app,db)
maneger=Manager(app)
maneger.add_command('db',MigrateCommand)
if __name__ == '__main__':
	maneger.run()