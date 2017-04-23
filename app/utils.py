from flask import request
from flask_wtf import FlaskForm
from urllib.parse import urlparse, urljoin
from wtforms_alchemy import model_form_factory

from app.models import db

### FORM TEMPLATE #####################################################
BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    """Base model form to inherit.

    It is set up to integrate wtforms_alchemy.
    """

    @classmethod
    def get_session(self):
        return db.session


### URL INTERNAL REDIRECT CHECK #######################################
def is_safe_url(target_url: str) -> bool:
    """Check to see if a URL redirects within the website.

    Code written by http://flask.pocoo.org/snippets/62/
    It is intended to prevent open redirects.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target_url))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
