from datetime import datetime

from flask import Blueprint, request, send_file
from ..model.user_model import user_model

user_api = Blueprint('user_api', __name__)

obj = user_model()


@user_api.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


@user_api.route("/user/create", methods=["POST"])
def user_create_controller():
    return obj.user_create_model(request.form)


@user_api.route("/user/update", methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)


@user_api.route("/user/delete/<id>", methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)


@user_api.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form, id)


@user_api.route("/user/getall/limit/<int:limit>/page/<int:page>", methods=["GET"])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit, page)


@user_api.route("/user/<uid>/upload/avatar", methods=["PUT"])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']
    # file.save(file.filename)
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "")

    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit) - 1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    # file.save(f"uploads/{uniqueFileName}.{ext}")
    return obj.user_upload_avatar_model(uid, finalFilePath)

@user_api.route("/uploads/<filename>")
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")
