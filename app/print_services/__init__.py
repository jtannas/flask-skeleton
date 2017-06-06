"""
Sample printing request webform.

This module is a sample WTForm based webform that I whipped up for a
friend that was interested in automating the process of submitting a
request to their print services department at work.
"""

from flask import Blueprint

print_services = Blueprint(
    'print_services',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/print_services/static/')

# Views Import; Circular; see http://flask-.readthedocs.io/en/latest/patterns/packages/
from .views import *
