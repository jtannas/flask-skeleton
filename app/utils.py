"""
Assorted utilities classes & functions for the Flask application.

This is a file for 'generically useful' classes and functions for the
Flask Application. The sort of stuff that could potentially be used in
sections of the python code, but don't necessarily belong to any one
part of the application.
"""

### IMPORTS ###################################################################
from urllib.parse import urlparse, urljoin

from fake import Factory
from flask import request
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory

from app.models import db, User

### FORM TEMPLATE #############################################################
BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    """
    Base model form to inherit when making other forms.

    It is set up to integrate wtforms_alchemy.
    """

    @classmethod
    def get_session(self):
        return db.session


### FUNCTIONS #################################################################
def is_safe_url(target_url: str) -> bool:
    """
    Check to see if a URL redirects within the website.

    Code written by http://flask.pocoo.org/snippets/62/
    It is intended to prevent open redirects.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target_url))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def populate_users(num_users=0):
    """
    Fills the database with fake users data.
    """
    from faker import Factory
    from app.models import User

    fake = Factory.create()

    admin = User()
    admin.name = 'jtannas'
    admin.email = 'jtannas@gmail.com'

    users = [admin]
    for _ in range(int(num_users)):
        new_user = User()
        new_user.email = fake.email()
        new_user.name = fake.userName()
        users.append(new_user)

    for user in users:
        db.session.add(user)

    db.session.commit()
