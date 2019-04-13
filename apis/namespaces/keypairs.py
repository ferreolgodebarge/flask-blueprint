from flask_restplus import Namespace, Resource, fields

api = Namespace("keypairs", description="Keypairs related operations")

keypair = api.model(
    "Keypairs",
    {
        "id": fields.String(required=True, description="The keypair identifier"),
        "name": fields.String(required=True, description="The keypair name"),
    },
)

KEYPAIRS = [{"id": "1a2b-3c4d-5e6f-7g8h", "name": "default_keypair"}]


@api.route("/")
class ServerList(Resource):
    @api.doc("list_keypairs")
    @api.marshal_list_with(keypair)
    def get(self):
        """List all keypairs"""
        return KEYPAIRS


@api.route("/<id>")
@api.param("id", "The keypair identifier")
@api.response(404, "Server not found")
class Server(Resource):
    @api.doc("get_keypair")
    @api.marshal_with(keypair)
    def get(self, id):
        """Fetch a keypair given its identifier"""
        for keypair in KEYPAIRS:
            if keypair["id"] == id:
                return keypair
        api.abort(404)
