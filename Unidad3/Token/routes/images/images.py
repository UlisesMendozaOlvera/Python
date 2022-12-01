from flask import Blueprint,request,jsonify
from sqlalchemy import exc
from models import Images
from app import db
from auth import tokenCheck
import base64

imageUser=Blueprint('imageUser',__name__,template_folder="templates")

def render_image(data):
    render_pic = base64.b64encode(data).decode('ascii')
    
@imageUser.route("/perfil",methods=["POST"])
@tokenCheck
def upload(usuario):
    searchImage=Images.query.filter_by(user_id=usuario["usuario_id"]).firsh()
    try:
        if searchImage:
            file=request.files["inputFile"]
            data=file.read()
            render_file=render_image(data)
            searchImage.rendered_date=render_file
            searchImage.data=data
            db.session.commit()
            return jsonify({"mensaje":"imagen actualizada"})
        else:
            file=request.files["inputFile"]
            data=file.read()
            render_file=render_image(data)
            newFile=render_image(data)
            newFile.type="Perfil"
            newFile.rendered_date=render_file
            newFile.user_id=usuario["user_id"]
            newFile.data=data
            db.session.add(newFile)
            db.session.commit()
            
            return jsonify({"mensaje":"imagen agregada"})
    except exc.SQLAlchemyError as e:
        print(e)
        return jsonify({"mensaje":"Error"})