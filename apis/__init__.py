from .v1 import blueprint as v1
from .v2 import blueprint as v2


def init_app(app):
    app.register_blueprint(v1)
    app.register_blueprint(v2)
