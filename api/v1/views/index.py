#!/usr/bin/python3
"""Module for app_views /status route"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/url', methods=['GET'])
def status():
"""Returns the status of /status route"""
    return (jsonify({'status':'ok'}))