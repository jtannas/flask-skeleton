"""
This module is part of implementing Flask-Script.

The Flask-Script extension provides support for writing external
scripts in Flask. This includes running a development server, a
customised Python shell, scripts to set up your database, cronjobs, and
other command-line tasks that belong outside the web application itself.

The runserver command is not intended to be used for running a
production server.
"""
### IMPORTS & INITS ###########################################################
import os

from flask_script import Server, Manager
from flask_migrate import MigrateCommand

from app import create_app
from app.config import CONFIGS
from app.models import db
from app.utils import populate_users

manager = Manager(create_app)

### COMMANDS & OPTIONS ########################################################
manager.add_option(
    '-m',
    '--mode',
    dest='mode',
    required=False, )

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0", port=8080))


@manager.command
@manager.option('-n', '--num_users', help='Number of users')
def create_db(num_users=0):
    """Creates database tables and populates them."""
    db.create_all()
    populate_users(num_users=num_users)


### RUN MAIN ##################################################################
if __name__ == '__main__':
    manager.run()
