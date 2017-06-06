"""Tests whether the application __init__ file works properly."""

### IMPORTS ###################################################################
from app import create_app
from app.config import CONFIGS


### TESTS #####################################################################
def test_create_app():
    """
    Tests whether the app can be created with all configurations given
    in the config file.
    """

    for name, mode in CONFIGS.items():
        create_app(mode=config)
