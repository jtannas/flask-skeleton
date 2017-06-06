"""
WTForm Definitions for the print services module.

See the __init__ file for more general info about the module.
"""
### IMPORTS AND CONSTANTS #####################################################
from flask import current_app
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

from app.utils import ModelForm

NONE = ('none', 'None')
OTHER = ('other', 'Other - Please specify in comments')

ALLOWED_EXTENSIONS = set([
    'txt',
    'pdf',
    'png',
    'jpg',
    'jpeg',
    'gif',
    'doc',
    'docx',
    'gdoc',
    'gsheet',
    'xls',
    'xlsm',
])


### FORMS #####################################################################
class PrintRequest(ModelForm):
    """
    Form for request print services.

    Allows a person to specify the options they want when printing
    through EPSB print services.
    Created using the WTForm framework.
    """
    number_of_copies = IntegerField(
        'Number of Copies',
        validators=[
            DataRequired(),
        ], )

    orientation = SelectField(
        'Orientation',
        choices=[
            ('portrait', 'portrait'),
            ('landscape', 'landscape'),
        ], )

    duplex = SelectField(
        'Single or Double Sided',
        choices=[
            ('flip-long', 'Flip on Long Edge'),
            ('flip-short', 'Flip on Short Edge'),
            ('single', 'Single Sided'),
            OTHER,
        ], )

    print_colour = SelectField(
        'Ink Color',
        choices=[
            ('black', 'Black and White'),
            ('gray', 'Grayscale'),
            ('colour', 'Full Colour'),
            OTHER,
        ], )

    paper_size = SelectField(
        'Paper Size',
        choices=[
            ('letter', 'Letter - 8.5" x 11"'),
            ('legal', 'Legal - 8.5" x 14"'),
            ('ledger', 'Ledger - 11" x 17"'),
            OTHER,
        ], )

    paper_type = SelectField(
        'Paper Type',
        choices=[
            ('plain', 'Plain White'),
            ('coloured', 'Coloured Paper - Please specify in comments'),
            ('matte', 'Matte Paper'),
            ('photo', 'Photo Paper'),
            ('cardstock', 'Card Stock'),
            OTHER,
        ], )

    laminate = BooleanField('Laminate?')

    punch = SelectField(
        'Hole Punch?',
        choices=[
            NONE,
            ('short', 'Short Edge'),
            ('long', 'Long Edge'),
            OTHER,
        ], )

    binding = SelectField(
        'Binding Method',
        choices=[
            NONE,
            ('staple_left_top', 'Staple - Left Top Corner'),
            ('staple_right_top', 'Staple - Right Top Corner'),
            ('staple_left_bottom', 'Staple - Left Bottom Corner'),
            ('staple_right_bottom', 'Staple - Right Bottom Corner'),
            ('booklet_coil', 'Booklet - Coil Binding'),
            ('booklet_staple', 'Booklet - Fold & Staple Center Line'),
            OTHER,
        ], )

    due_date = DateField(
        'When do you need it by?',
        validators=[
            DataRequired(),
        ], )

    exam = BooleanField('Is this an exam?')

    printme = FileField(
        'File to make copies of',
        validators=[
            FileRequired(),
            FileAllowed(ALLOWED_EXTENSIONS,
                        'That type of file is not permitted!'),
        ], )

    cover = FileField(
        'Cover Slip - Optional',
        validators=[
            FileAllowed(ALLOWED_EXTENSIONS,
                        'That type of file is not permitted!'),
        ], )

    comments = TextAreaField(
        'Comments and additonal instructions',
        validators=[
            Length(max=4096),
        ], )
