from flask import Blueprint
from flask_restplus import Api
from apis.servers import api as servers

blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(blueprint,
        title='Manage compute resources',
        version='1.0',
        description='Servers management',
)

api.add_namespace(servers)
