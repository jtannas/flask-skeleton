"""
The website views for the print services module.

See the __init__ file for general info about the module.
"""

### IMPORTS ###################################################################
from flask import flash, current_app, session, redirect, render_template, \
    request, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
import os

from app.extensions import cache, limiter, login_manager
from app.models import db, User

from ..print_services import print_services
from .forms import PrintRequest


### VIEWS #####################################################################
@print_services.route('/request_print', methods=['GET', 'POST'])
@login_required
def serve_request_form():
    """Serves and processes the print request form.

    The process for handling the form data depends on the deployment.
    """
    form = PrintRequest()
    if form.validate_on_submit():
        f = form.printme.data
        filename = secure_filename(f.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        flash('Success!')
    return render_template('request_print.html', form=form)
