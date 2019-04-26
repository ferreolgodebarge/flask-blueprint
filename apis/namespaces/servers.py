from flask_restplus import Namespace, Resource, fields, marshal_with
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

server_error = api.model(
    "Error",
    {
        "status": fields.String(required=True, description="Failure status"),
        "message": fields.String(required=True, description="Failure message"),
    }
)


@api.route("/")
class ServerList(Resource):
    @api.doc("list_servers")
    @api.marshal_list_with(server, code=200, description='Success')
    def get(self):
        """List all servers"""
        return list_servers()

    @api.doc("create_server")
    @api.expect(server_request)
    @api.marshal_with(server, code=201, description='Created')
    def post(self):
        """Crete a server with its name"""
        return create_server(api.payload["name"], api.payload["description"])


@api.route("/<id>")
@api.param("id", "The server identifier")
class Server(Resource):
    @api.doc("get_server")
    @api.marshal_with(server, code=200, description='Success')
    @api.marshal_with(server_error, code=404, description='Not found')
    def get(self, id):
        """Fetch a server given its identifier"""
        return get_server_by_id(id)

    @api.doc("update_server")
    @api.expect(server_request)
    @api.marshal_with(server)
    def put(self, id):
        """Update a server given its identifier"""
        return update_server(id, api.payload["name"], api.payload["description"])

    @api.doc("delete_server")
    def delete(seld, id):
        """Delete a server given its identifier"""
        return delete_server(id)
