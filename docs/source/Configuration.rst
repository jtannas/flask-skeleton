Application Configuration
=========================

The Flask framework supports many different ways of setting the
configuration. Not all of these are supported by all hosting services
though.

For awhile, I went with having an app/config.py file that handled all
the generic & 'non-secret' settings, along with an instance/flask_config.py
file for private setting (eg. secret keys). It was a pain in the butt
to get going, but it worked eventually.

The problem with that is that is requires an instance folder that sits
in the same parent directory as the application, but isn't commited to
version management. This doesn't work for services like Heroku where
the application is deployed via a git push.

I eventually settled on having all of the configuration settings being
in the app/config.py file, and having that file pull sensitive settings
from OS environment varibles. The environment variables are fairly easy
to set on a development workstation using autoenv and a .env file.


Appplication Modes
------------------

Within the config.py, there are couple different classes. The 'Default'
class contains all the default settings for the application. As of the
writing of this documentation there are also classes for:

- Development
- Testing
- Production

These classes each inherit the default class, and then modify certain
variables. They each represent a different 'mode' for the application:

- development mode
- testing mode
- production mode

The flask application then draws it's configuration from a mode. Heroku
has the mode specified by name via an environment variable (see the
Procfile). The manage.py file supports choosing the mode via the -m option.