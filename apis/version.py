from flask import Blueprint
from flask_restplus import Api
from apis.namespaces.version import api as version

blueprint = Blueprint("version", __name__)#, url_prefix="/")

api = Api(
    blueprint,
    title="Manage compute resources",
    version="0.1",
    description="Servers management",
)

api.add_namespace(version)
