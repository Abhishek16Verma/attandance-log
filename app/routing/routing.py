from flask_restful import Api
from services.user import User
from services.logging import Capture, VerifyImg


def get_route_map(app):
    return [
        {   'obj': User,
            'pattern': ['/create-user'],        
        },
        {   'obj': Capture,
            'pattern': ['/capture'],        
        },
        {   'obj': VerifyImg,
            'pattern': ['/login'],        
        }
    ]


def routing(app):
    route_map = get_route_map(app)
    for obj in route_map:
        api = Api(app)
        api.add_resource(obj['obj'], *obj['pattern'])

