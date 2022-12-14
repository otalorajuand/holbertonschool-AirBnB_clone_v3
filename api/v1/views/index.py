#!/usr/bin/python3
"""Module for app_views /status route"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/url', methods=['GET'])
def status():
    """Returns the status of /status route"""
    return (jsonify({'status':'ok'}))


@app_views.route('/api/v1/stats')
def stats():
    """Returns the number of each objects by type"""
    objects = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(objects)