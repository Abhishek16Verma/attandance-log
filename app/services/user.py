
from flask_restful import Resource
from flask import  request
from utils.logger import FileLogs
import json
import os


userpath = os.getenv("USER_JSON_DATABASE")
logs = FileLogs().get_logger()

class User(Resource):

    def __init__(self):
        self._file = open(userpath, 'r')
        self._user = json.load(self._file)
        # with open('/home/abhishekverma/bak-abhishek/attendance-log/app/json_params/role.json', 'r') as json_role:
        #     self._role = json.loads(json_role)
    def __del__(self):
        self._file.close()
        
    def post(self):
        user_role = {"roleid":1}
        key = os.getenv("SECRET_KEY")
        try:
            
            if request.method == "POST":
                user_data = request.json
                if len(user_data.keys()) < 2:
                    logs.error(f"error in User not fill all the fields {__file__}", exc_info=1)
                    return {"error": "fill all the parameters"}
                username = user_data["username"]
                user = {}
                if username not in self._user:
                    if user_data["secret_key"] == key:
                        user_role = {"roleid":0}
                    user_role.update(user_data)
                    user[username] = user_role
                    self._user.update(user)
                    print(self._user,"---------------")
                    with open(userpath, 'w') as json_file:
                        json.dump(self._user, json_file, indent=4)
                    return {"msg":"account created...."}
                else:
                    return {"msg":"user alreday exist...."}


        except Exception as e:
            logs.error(f"error in User {__file__}", exc_info=1)
            return {"message":"Exception error in post request"}, 500
        
        