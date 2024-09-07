
from flask_restful import Resource
from flask import  render_template,make_response,session,Response
from flask_httpauth import HTTPBasicAuth
from utils.logger import FileLogs
from modules.capture import capture_face
import json
import os

logs = FileLogs().get_logger()
auth = HTTPBasicAuth()
userpath = os.getenv("USER_JSON_DATABASE")

class UserAuth:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self._user = json.load(file)

    def verify_user(self, username, password):
        if username in self._user:
            if self._user[username]["password"] == password:
                return username
            return "please enter correct username/password"


@auth.verify_password
def verify_password(username, password):
    user_auth = UserAuth(userpath)
    return user_auth.verify_user(username, password)

# class Login(Resource):
    
   
        
class Capture(Resource):
    usr = None

    @auth.login_required
    def get(self):
        try:
            success = f"Hello, {auth.current_user()}!, click Your Snap"
            return make_response(render_template('index.html', data = success))
        except Exception as e:
            logs.error(f"error in User {__file__}", exc_info=1)
            return {"message":"Exception error in post request"}, 500 
    @auth.login_required
    def post(self):
        try:
            img = f"{auth.current_user()}.png"
            self._verify_image = capture_face(img)
            return "Image successful save"
        except Exception as e:
            logs.error(f"error in User {__file__}", exc_info=1)
            return {"message":"Exception error in post request"}, 500

class VerifyImg(Resource):
    @auth.login_required
    def get(self):
        try:
            varify_usr = auth.current_user()
            return (make_response(render_template("verify.html", data = varify_usr)))
        except Exception as e:
            logs.error(f"error in User {__file__}", exc_info=1)
            return {"message":"Exception error in post request"}, 500
    
    # @auth.login_required
    # def post(self):
    #     session.pop('username', None)  
    #     response = Response('You have been logged out.', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    #     return response
