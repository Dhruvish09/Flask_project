import json
import mysql.connector
from flask import make_response


class user_model():
    def __init__(self):
        # Connection establishment code
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", password="dp612000",
                                               database="Flask_Rest_Api")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some Error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()

        if len(result) > 0:
            res = make_response({"payload": result}, 200)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            return make_response({"Message": "No record found."}, 404)

    def user_create_model(self, data):
        self.cur.execute(
            f"INSERT INTO users(name,email,phone,role,password) value('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        return make_response({"Message": "User Created Successfully."}, 201)

    def user_update_model(self, data):
        self.cur.execute(
            f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']} ")
        if self.cur.rowcount > 0:
            return make_response({"Message": "User Updated Successfully."}, 201)
        else:
            return make_response({"Message": "Nothing to update."}, 202)

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"Message": "User Deleted Successfully."}, 200)
        else:
            return make_response({"Message": "Provided ID is not exist."}, 202)

    def user_patch_model(self, data, id):
        qry = "UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
            # qry = qry + f"{key}={data[key]}, "
        qry = qry[:-1] + f" WHERE id={id}"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"Message": "User Partially Updated Successfully."}, 201)
        else:
            return make_response({"Message": "Nothing to update."}, 202)

    def user_pagination_model(self, limit, page):
        print(type(limit))
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"

        self.cur.execute(qry)
        result = self.cur.fetchall()

        if len(result) > 0:
            res = make_response({"payload": result, "Page_no": page, "limit": limit}, 200)
            return res
        else:
            return make_response({"Message": "No record found."}, 204)

    def user_upload_avatar_model(self, uid, filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount > 0:
            return make_response({"Message": "File Uploaded Successfully."}, 201)
        else:
            return make_response({"Message": "Nothing to upload."}, 202)
