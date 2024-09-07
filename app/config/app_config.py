from flask import Flask
import os
from routing.routing import routing

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    routing(app)
    return app
