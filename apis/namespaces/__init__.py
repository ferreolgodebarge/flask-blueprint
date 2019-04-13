from flask_restplus import Api

from .servers import api as servers

api = Api(
    title="My Title",
    version="1.0",
    description="A description",
    # All API metadatas
)

api.add_namespace(servers)
