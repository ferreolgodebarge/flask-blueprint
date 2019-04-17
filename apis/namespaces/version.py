from flask_restplus import Namespace, Resource, fields

api = Namespace("version", description="Display API version")

VERSION = {
    "package_version": "1.2.3",
    "/version": {
        "version": "0.1",
        "name": "version",
        "doc": "/documentation",
        "description": "My description v1",
    },
    "available_versions": [
        {
            "version": "1.0",
            "name": "v1",
            "doc": "/v1/documentation",
            "description": "My description v1",
        },
        {
            "version": "2.0",
            "name": "v1",
            "doc": "/v1/documentation",
            "description": "My description v1",
        },
    ],
    "hostname": "127.0.0.1",
}


@api.route("/")
class Version(Resource):
    @api.doc("get_version")
    def get(self):
        """Display version"""
        return VERSION
