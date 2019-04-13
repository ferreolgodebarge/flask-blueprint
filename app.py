from flask import Flask
from models import db, init_app
import apis


def create_app():
    app = Flask(__name__)
    with app.test_request_context():
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        db.init_app(app)
        db.create_all()
        apis.init_app(app)
    return app


app = create_app()
app.run(host="0.0.0.0", debug=True)
