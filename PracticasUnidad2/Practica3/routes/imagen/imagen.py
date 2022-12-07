from flask import Blueprint, request,jsonify,render_template
from sqlalchemy import exc
from models import User
from app import db,bcrypt
from auth import tokenCheck
import base64 

imageUser = Blueprint('imageUser',__name__,template_folder="templates")

def render_image(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

# @imageUser.route("/displayImage", methods=["GET"])
# @tokenCheck
# def displayImage(usuario):
#         searchImage = User.query.filter_by(id = usuario['user_id']).first()
#         if searchImage:
#             image = searchImage.rendered_data
#             return render_template('PerfilUsuario.html',img_data=image)
#         else:
#             return jsonify({"message":"No image"})

