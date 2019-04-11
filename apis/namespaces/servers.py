from flask_restplus import Namespace, Resource, fields

api = Namespace('servers', description='Servers related operations')

server = api.model('Server', {
    'id': fields.String(required=True, description='The server identifier'),
    'name': fields.String(required=True, description='The server name'),
})

SERVERS = [
    {'id': '1a2b-3c4d-5e6f-7g8h', 'name': 'default_server'},
]

@api.route('/')
class ServerList(Resource):
    @api.doc('list_servers')
    @api.marshal_list_with(server)
    def get(self):
        '''List all servers'''
        return SERVERS

@api.route('/<id>')
@api.param('id', 'The server identifier')
@api.response(404, 'Server not found')
class Server(Resource):
    @api.doc('get_server')
    @api.marshal_with(server)
    def get(self, id):
        '''Fetch a server given its identifier'''
        for server in SERVERS:
            if server['id'] == id:
                return server
        api.abort(404)
