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
    #@api.marshal_list_with(server, code=200, description='Success')
    @api.response(code=200, description='Success', model=[server])
    def get(self):
        """List all servers"""
        return list_servers(), 200

    @api.doc("create_server")
    @api.expect(server_request)
    @api.response(code=201, description='Created', model=server)
    @api.response(code=409, description='Server already exists.', model=server_error)
    def post(self):
        """Crete a server with its name"""
        res = create_server(api.payload["name"], api.payload["description"])
        if res:
            return res, 201
        else:
            return {"status": "fail", "message": "Server already exists with this name."}, 409


@api.route("/<id>")
@api.param("id", "The server identifier")
class Server(Resource):
    @api.doc("get_server")
    @api.response(code=200, description='Success', model=server)
    @api.response(code=404, description='Not found', model=server_error)
    def get(self, id):
        """Fetch a server given its identifier"""
        res = get_server_by_id(id)
        if res:
            return res, 200
        else: 
            return {"status": "fail", "message": "Server with id {} not found.".format(id)}, 404

    @api.doc("update_server")
    @api.expect(server_request)
    @api.response(code=200, description='Success', model=server)
    @api.response(code=404, description='Server not found', model=server_error)
    def put(self, id):
        """Update a server given its identifier"""
        res = update_server(id, api.payload["name"], api.payload["description"])
        if res:
            return res, 200
        else:
            return {"status": "fail", "message": "Server does not exist."}, 404

    @api.doc("delete_server")
    @api.response(code=204, description='Deleted')
    @api.response(code=404, description='Not found', model=server_error)
    def delete(seld, id):
        """Delete a server given its identifier"""
        res = delete_server(id)
        if res == 204:
            return '' ,204
        else:
            return {"status": "fail", "message": "Server does not exist."}, 404

