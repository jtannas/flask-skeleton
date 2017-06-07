#!/usr/bin/env python
"""
Init file for the flask application.

This contains the flask factory functions, but does not actually run
anything. This is to allow for better control over the application
during testing and deployment.
"""

### IMPORTS ###################################################################
from flask import Flask, redirect, render_template, request
from flask_login import login_required
from flask_sslify import SSLify
from flask_wtf.csrf import CSRFError

from app.config import CONFIGS
from app.extensions import cache, csrf, debug_toolbar, limiter, login_manager, \
    migrate
from app.models import db

### IMPERATIVE SHELL ##########################################################
def create_app(mode=None):
    """
    Create, configure, extend, and add blueprints to a flask instance.

    Args:
        name (str): the name for the flask application.
        mode (str): Specifies the configuration mode from the app.config.
        instance_config_pyfile (str): Specifies the which <config>.py file
            to use in the instance folder.

    Returns:
        app (Flask): a Flask instance

    Raises:
        AssertError (Exception): If the instance configuration flag is
            not set, indicating that the instance configuration was not
            complete.
        AttributeError (Exception): module config has no attribute
            <config_module>. This indicates that the provided
            <config_module> is not a match for a config classes.
            in the config package.

    """
    ### Function Defaults
    # Flask-script passes None when given no arguments
    if not mode:
        mode = 'Default'

    ### Init the application
    app = Flask(__name__)
    app.config.from_object(CONFIGS[mode])

    ### Register modifications to the app
    register_debugtools(app)
    register_errorhandlers(app)
    register_extensions(app)
    register_blueprints(app)

    ### Define the index route
    @app.route('/', methods=['GET'])
    @login_required
    @cache.cached(timeout=60)
    def index():
        return render_template('index.html')

    ### Complete
    return app

### FUNCTIONAL CORE ###########################################################
def register_debugtools(flask_app):
    """
    Applies some extra configuration changes for debug mode.
    """

    if flask_app.config['DEBUG'] is False:
        return

    debug_toolbar.init_app(flask_app)

    @flask_app.after_request
    def after_request(response):
        """Modifies the response header to prevent caching."""
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Expires'] = 0
        response.headers['Pragma'] = "no-cache"
        return response


def register_extensions(flask_app):
    """Extends the flask application with useful extensions.

    It modifies the application in place, but the app is returned for
    more general usage.

    Args:
        flask_app (Flask): flask application instance

    Returns:
        None
    """
    cache.init_app(flask_app, config={'CACHE_TYPE': 'simple'})
    csrf.init_app(flask_app)
    db.init_app(flask_app)

    @flask_app.before_first_request
    def create_db_objects():
        db.create_all()

    login_manager.init_app(flask_app)
    migrate.init_app(flask_app, db)
    SSLify(flask_app)  # the init_app method doesn't seem to work correctly

def register_blueprints(flask_app):
    """Registers chosen blueprints to the flask application instance.

    It modifies the application in place, but the app is returned for
    more general usage.

    Args:
        flask_app (Flask): flask application instance

    Returns:
        None
    """

    from app.auth import auth
    flask_app.register_blueprint(auth)

def register_errorhandlers(flask_app):
    """Registers error handlers for a list of errors."""

    def render_error(e):
        if hasattr(e, 'code'):
            return render_template(f'errors/{e.code}.html'), e.code
        else:
            return render_template(f'errors/500.html'), 500

    for e in [403, 404, 410, 500, CSRFError]:
        flask_app.errorhandler(e)(render_error)
