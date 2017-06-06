#!/usr/bin/env python
"""
Init file for the flask application.

This contains the flask factory functions, but does not actually run
anything. This is to allow for better control over the application
during testing and deployment.
"""
from flask import Flask, redirect, render_template, request
from flask_login import login_required
from flask_sslify import SSLify
from flask_wtf.csrf import CSRFError

from app.config import CONFIGS
from app.extensions import cache, csrf, debug_toolbar, limiter, login_manager
from app.models import db

def create_app(config=CONFIGS['Default']):
    """
    Create, configure, extend, and add blueprints to a flask instance.

    Args:
        name (str): the name for the flask application
        config_module (str): Specifies the configuration module in the
            config folder.

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

    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(config)
    app.config.from_pyfile('flask_config.py')
    assert app.config['INSTANCE_CONFIG_COMPLETE'] is True, \
        "Failed to find instance configuration file"

    register_debugtools(app)
    register_errorhandlers(app)
    register_extensions(app)
    register_blueprints(app)

    @app.route('/', methods=['GET'])
    @login_required
    @cache.cached(timeout=60)
    def index():
        return render_template('index.html')

    return app


def register_debugtools(flask_app):
    """Applies some extra configuration changes for debug mode"""

    if flask_app.config['DEBUG'] is False:
        return

    # debug_toolbar.init_app(flask_app)

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
    SSLify(flask_app)  # the init_app method doesn't seem to correctly

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
    """Registers error handlers for a list of errors"""

    def render_error(e):
        return render_template(f'errors/{e.code}.html'), e.code

    for e in [403, 404, 410, 500, CSRFError]:
        flask_app.errorhandler(e)(render_error)