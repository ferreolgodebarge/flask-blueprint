from flask import Flask
from apis.v1 import blueprint as v1
from apis.v2 import blueprint as v2

app = Flask(__name__)

app.register_blueprint(v1)
app.register_blueprint(v2)
app.run(host='0.0.0.0', debug=True)
