
from flask import Flask
from database import db 
from flask_migrate import Migrate
from models import Persona
app= Flask(__name__)

USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='flask_db'
FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']=FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

migrate=Migrate()
migrate.init_app(app,db) #flask db init 
#flask db migrate
#flask db upgrade