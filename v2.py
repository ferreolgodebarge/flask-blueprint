from flask import Blueprint
from flask_restplus import Api
from apis.servers import api as servers
from apis.keypairs import api as keypairs

blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(blueprint,
        title='Manage compute resources',
        version='2.0',
        description='Servers and keypairs management',
)

api.add_namespace(servers)
api.add_namespace(keypairs)
