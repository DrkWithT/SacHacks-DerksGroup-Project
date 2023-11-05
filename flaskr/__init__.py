"""
    @file __init__.py\n
    Contains startup code for our web application.\n
"""

import os

from flask import Flask, render_template
# NOTE We may use PyMongo to use the container's MongoDB instance available.

from flaskr.components.pages import page_router
from flaskr.components.routes import ajax_router

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load configured settings from a config.py script if present.
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    # Ensure instance/ directory exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(404)
    def handle_wrong_route(error):
        return render_template('oops.html', page_title='Oops Page')

    # NOTE This requires the HTML pages to be in the templates folder. Dynamic data can be inserted with Jinja template syntax from the Flask docs. 
    app.register_blueprint(page_router)

    # NOTE This requires AJAX on the frontend to send request to the right route URL... See routes.py
    app.register_blueprint(ajax_router)

    # Export app object to runner.
    return app
