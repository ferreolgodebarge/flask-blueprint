from flask_restplus import Namespace, Resource, fields
from core.servers import (
    list_servers,
    create_server,
    get_server_by_id,
    update_server,
    delete_server,
)


api = Namespace("servers", description="Servers related operations", ordered=True)

server = api.model(
    "Server",
    {
        "id": fields.String(required=True, description="The server identifier"),
        "name": fields.String(required=True, description="The server name"),
        "description": fields.String(
            required=True, description="The server description"
        ),
    },
)

server_request = api.model(
    "Server request",
    {
        "name": fields.String(required=True, description="The server name"),
        "description": fields.String(description="The server description"),
    },
)


@api.route("/")
class ServerList(Resource):
    @api.doc("list_servers")
    def get(self):
        """List all servers"""
        return list_servers()

    @api.doc("create_server")
    @api.expect(server_request)
    def post(self):
        """Crete a server with its name"""
        return create_server(api.payload["name"], api.payload["description"])


@api.route("/<id>")
@api.param("id", "The server identifier")
class Server(Resource):
    @api.doc("get_server")
    def get(self, id):
        """Fetch a server given its identifier"""
        return get_server_by_id(id)

    @api.doc("update_server")
    @api.expect(server_request)
    def put(self, id):
        """Update a server given its identifier"""
        return update_server(id, api.payload["name"], api.payload["description"])

    @api.doc("delete_server")
    def delete(seld, id):
        """Delete a server given its identifier"""
        return delete_server(id)
