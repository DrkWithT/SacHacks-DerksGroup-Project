"""
    pages.py\n
    Separate part of the Flask code to serve HTML template pages.
"""

from flask import Blueprint

# This router will be set onto the app in __init__.py later.
page_router = Blueprint('page_router', __name__)

# Put request handlers to send back pages.
@page_router.route('/', methods=['GET', 'POST'])
def serve_homepage():
    return '<h2>Home Page</h2><p>Hello World</p>'

# TODO add more routing functions here to call render_template(<template file name>, <dict of data>) as a server-side rendered reply.
