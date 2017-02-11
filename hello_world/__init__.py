# -*- coding: utf-8 -*-
from flask import Flask
# from flaskext.mysql import MySQL

app = Flask(__name__)
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = '14_dam'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'katrin18'
# app.config['MYSQL_DATABASE_DB'] = 'flask'
# app.config['MYSQL_DATABASE_HOST'] = 'wierzba.wzks.uj.edu.pl'
# mysql.init_app(app)

from hello_world import views
#asd
