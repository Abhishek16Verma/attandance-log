import os
import mysql.connector
from dotenv import load_dotenv
from utils.logger import FileLogs

load_dotenv('.env')

logs = FileLogs().get_logger()
class Db:
    def __init__(self):

        self.conn_user = None
        self.conn_role = None
        self.conn_user_image = None
        self.conn_permission = None
        self.HOST_NAME = os.getenv('HOST')
        self.USER = os.getenv('USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.USER_DATABASE = os.getenv('USER_DATABASE')
        self.ROLE_DATABASE = os.getenv('ROLE_DATABASE')
        self.PERMISSION_DATABASE = os.getenv('PERMISSION_DATABASE')
        self.USER_IMAGE = os.getenv('USER_IMAGE')


    def get_connection_user(self):
        if self.conn_user is None:
            try:
                self.conn_user = mysql.connector.connect(
                    host = self.HOST_NAME,
                    database = self.USER_DATABASE,
                    user = self.USER,
                    password = self.PASSWORD
                )
            except Exception as e:
                logs.error("error in connection", exc_info=1)
                return None
        return self.conn_user
    
    # connection for contentsite db
    def get_connection_role(self):
        if self.conn_role is None:
            try:
                self.conn_role = mysql.connector.connect(
                    host = self.HOST_NAME,
                    database = self.ROLE_DATABASE,
                    user = self.USER,
                    password = self.PASSWORD
                )
            except Exception as e:
                logs.error("error in connection", exc_info=1)
                return None
        return self.conn_role

    def get_connection_permission(self):
        if self.conn_permission is None:
            try:
                self.conn_permission = mysql.connector.connect(
                    host = self.HOST_NAME,
                    database = self.PERMISSION_DATABASE,
                    user = self.USER,
                    password = self.PASSWORD
                )
            except Exception as e:
                logs.error("error in connection", exc_info=1)
                return None
        return self.conn_permission
    
    def get_connection_user_image(self):
        if self.conn_user_image is None:
            try:
                self.conn_user_image = mysql.connector.connect(
                    host = self.HOST_NAME,
                    database = self.USER_IMAGE,
                    user = self.USER,
                    password = self.PASSWORD
                )
            except Exception as e:
                logs.error("error in connection", exc_info=1)
                return None
        return self.conn_user_image
   