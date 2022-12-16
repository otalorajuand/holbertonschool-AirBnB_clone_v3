#!/usr/bin/python3
"""Module for amenity endpoints"""
from flask import jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity


@app_views.route('/places/<place_id>/amenities',
                 strict_slashes=False, methods=['GET'])
def get_places_amenities(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if not place:
        return make_response(jsonify({"error": "Not found"}), 404)
    return jsonify([amenity.to_dict() for amenity in place.amenities])

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(place_id, amenity_id):
    """Deletes a Review object"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if not place:
        return make_response(jsonify({"error": "Not found"}), 404)
    if not amenity:
        return make_response(jsonify({"error": "Not found"}), 404)
    storage.delete(amenity)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 strict_slashes=False, methods=["POST"])
def post_amenity(place_id):
    """POST /place API route"""
    place = storage.get(Place, place_id)
    if not place:
        return make_response(jsonify({"error": "Not found"}), 404)
    if not amenity:
        return make_response(jsonify({"error": "Not found"}), 404)

    data = request.get_json(force=True, silent=True)
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if "text" not in data:
        return make_response(jsonify({"error": "Missing text"}), 400)
    if "user_id" not in data:
        return make_response(jsonify({"error": "Missing user_id"}), 400)


    data['place_id'] = place_id
    amenity = Amenity(**data)
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)
