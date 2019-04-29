from models import db
from models.servers import Servers
from core.id import generate


def list_servers():
    servers = Servers.query.all()
    response_object = []
    for server in servers:
        response_object.append(server.to_dict())
    return response_object


def get_server_by_id(id):
    server = Servers.query.filter_by(id=id).first()
    if server:
        response_object = {
            "id": server.id,
            "name": server.name,
            "description": server.description,
        }
        return response_object


def create_server(name, description):
    server = Servers.query.filter_by(name=name).first()
    if not server:
        uuid = str(generate())
        new_server = Servers(id=uuid, name=name, description=description)
        register_entry(new_server)
        response_object = {"id": uuid, "name": name, "description": description}
        return response_object


def update_server(id, name, description):
    server = Servers.query.filter_by(id=id).first()
    if server:
        server.name = name
        server.description = description
        db.session.commit()
        response_object = {
            "id": server.id,
            "name": server.name,
            "description": server.description,
        }
        return response_object


def delete_server(id):
    server = Servers.query.filter_by(id=id).first()
    if server:
        Servers.query.filter_by(id=id).delete()
        db.session.commit()
        return 204


def register_entry(server):
    db.session.add(server)
    db.session.commit()
