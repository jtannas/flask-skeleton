Forms Design
============

Flask-WTForms is used to create forms. There's a whole lot to learn
there, so I won't go into specifics of how to render a certain type of
field - that's what the documentation is for.

The main modification I've made is to use a jinja2 macro to render the
forms (see app/templates/builders/macros.html). The macro is called
render_field, and takes a wtform field as an argument. If there are any
validation errors, the errors are rendered as part of the field.