"""
    pages.py\n
    Separate part of the Flask code to serve HTML template pages.
"""

from flask import Blueprint, render_template

# This router will be set onto the app in __init__.py later.
page_router = Blueprint('page_router', __name__, template_folder='./templates')

# Put request handlers to send back pages.
@page_router.route('/', methods=['GET'])
def serve_homepage():
    return render_template('frontpage.html', page_title='Landing')
