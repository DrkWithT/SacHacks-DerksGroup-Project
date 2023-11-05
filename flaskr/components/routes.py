"""
    routes.py\n
    Contains a separate part of the Flask code to handle AJAX requests from the frontend. This should load arguments and alternate trip info.
"""

# NOTE this can be for parsing / writing JSON between frontend and backend. We may need PyMongo if we want to use MongoDB.
# import json
# import pymongo
from flask import Blueprint, request

from flaskr.data.mockdata import MOCK_DATA, DEFAULT_ERR_DATA
from flaskr.data.envars import MAPS_API_KEY

# Demo processing function (pretend the request is processed into data for Maps)
def demo_serve_data(args: dict=None):
    if args is None:
        return DEFAULT_ERR_DATA
    
    action = args['action']

    if action == 0:  # 0: get car collision risks
        return {'ok': True, 'key': MAPS_API_KEY, 'data': MOCK_DATA}
    elif action == 1:  # 1: get alternate route?
        return {'ok': True, 'key': MAPS_API_KEY, 'data': None}
    else:
        return DEFAULT_ERR_DATA

# This router will be set onto the app in __init__.py later.
ajax_router = Blueprint('ajax_router', __name__)

# Handle requests asking for location & risk points.
@ajax_router.route('/appapi/load')
def handle_risks_req():
    req_method = request.method
    req_json = None

    if request.is_json:
        req_json = request.get_json()

    if req_method == 'GET':
        return demo_serve_data(req_json)

    return DEFAULT_ERR_DATA

# Handle requests asking for a new route given car accidents.
@ajax_router.route('/appapi/trip')
def handle_trip_req():
    req_method = request.method
    req_json = None

    if request.is_json:
        req_json = request.get_json()

    if req_method == 'GET':
        return demo_serve_data(req_json)

    return DEFAULT_ERR_DATA
