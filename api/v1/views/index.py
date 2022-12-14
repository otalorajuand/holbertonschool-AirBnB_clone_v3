from api.v1.views import app_views
from flask import jsonify

@app_views.route('/url', methods=['GET'])
def status()
    return (jsonify({'status':'ok'}))