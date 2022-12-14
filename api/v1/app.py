#!/usr/bin/python3
"""
This module contains a flask app
"""
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', default="0.0.0.0")
    port = os.getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=port, threaded=True)