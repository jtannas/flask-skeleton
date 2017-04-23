"""Extensions module for the flask application

Useful for creating objects used by both the main application
(app.__init__.py) and by blueprint modules. By creating them here
instead, it reduces the occurence of circular imports.
"""

from flask_cache import Cache
cache = Cache()

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

from flask_debugtoolbar import DebugToolbarExtension
debug_toolbar = DebugToolbarExtension()

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
limiter = Limiter(key_func=get_remote_address)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
