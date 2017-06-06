"""
This module is part of implementing Flask-Script.

The Flask-Script extension provides support for writing external
scripts in Flask. This includes running a development server, a
customised Python shell, scripts to set up your database, cronjobs, and
other command-line tasks that belong outside the web application itself.
"""
### IMPORTS ###################################################################
import os

from flask_script import Server, Manager
from flask_migrate import MigrateCommand

from app import create_app
from app.config import CONFIGS

manager = Manager(create_app)

### COMMANDS & OPTIONS ########################################################
manager.add_option("-c", "--config", dest="config", required=False)
# Pass the command line option for -c/--config to the config argument
# of create_app.

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=8080))

### RUN MAIN ##################################################################
if __name__ == '__main__':
    manager.run()
