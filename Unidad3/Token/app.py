
from flask import Flask,request,jsonify 
from flask_cors import CORS
from database import db 
from encript import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from models import User
from sqlalchemy import exc
from functools import wraps
from routes.user.user import appuser
from routes.images.images import imageUser

app=Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(imageUser)

app.config.from_object(BaseConfig)
CORS(app)
db.init_app(app)
migrate=Migrate()
migrate.init_app(app,db)

