from flask import Flask
from models import db, init_app
import apis

def create_app():
    app = Flask(__name__)
    with app.test_request_context():
        #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        app.config.from_object('config.conf')
        db.init_app(app)
        db.create_all()
        apis.init_app(app)
    return app

def run_app(host='0.0.0.0', port=5000, debug=True):
    app = create_app()
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run_app()
