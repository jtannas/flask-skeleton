"""
Container for built-in configuration classes.

Each class contains constants that Flask can read into the configuration
of the application. A configuration class can inherit another one as a
starting point, so a Default class has been created.

You can override or extend these settings through the instance configuration.
"""
from os import environ


class Default():
    """
    Base configuration for the flask application.

    This configuration is meant as a 'baseline' set of configuration
    settings that is then overridden via more specific configurations.
    """
    from tempfile import gettempdir

    DEBUG = True

    #: Secret Key
    SECRET_KEY = environ['SECRET_KEY']

    #: Use server side sessions for greater security
    SESSION_FILE_DIR = gettempdir()
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'

    #: Define the SQLAlchemy database connection properties
    SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    #: Application threads. A common general assumption is using 2 per
    #: available processor core - to handle incoming requests using one and
    #: performing background operations using the other.
    THREADS_PER_PAGE = 2

    #: Enable protection against Cross-site Request Forgery (CSRF).
    CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = environ['WTF_CSRF_SECRET_KEY']

    #: ReCaptcha Settings
    RECAPTCHA_USE_SSL = True

    #: Set the Flask-Limter Rate limit options to prevent spamming
    RATELIMIT_GLOBAL = '1/second;20/minute;400/day'
    RATELIMIT_STRATEGY = 'fixed-window-elastic-expiry'

    #: File Upload Settings
    MAX_CONTENT_LENGTH = 32 * 1024**2
    UPLOAD_FOLDER = environ['UPLOAD_FOLDER']

    #: OAuth Settings
    OAUTH_CREDENTIALS = {
    'google': {
        'id': environ['GOOGLE_OAUTH_ID'],
        'secret': environ['GOOGLE_OAUTH_SECRET'],
    }
} # yapf: disable


class Development(Default):
    """Development configuration for the flask application."""
    DEBUG = True


class Testing(Default):
    """Testing configuration for the flask application."""
    DEBUG = False


class Production(Default):
    """Production configuration for the flask application."""
    DEBUG = False


CONFIGS = {
    'Default': Default,
    'Development': Development,
    'Testing': Testing,
    'Production': Production,
}
