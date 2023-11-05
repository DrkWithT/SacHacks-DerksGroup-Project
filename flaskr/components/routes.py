"""
    routes.py\n
    Contains a separate part of the Flask code to handle AJAX requests from the frontend.
"""

# NOTE this can be for parsing / writing JSON between frontend and backend. We may need PyMongo if we want to use MongoDB.
# import json
# import pymongo
from flask import Blueprint

# This router will be set onto the app in __init__.py later.
ajax_router = Blueprint('ajax_router', __name__)

# Put request handler for creating advisories to send back about traffic conditions at some time.
@ajax_router.route('/appapi/plan/make')
def handle_get_plan():
    return 'This is a test message.'
