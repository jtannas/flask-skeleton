Security
========

I'm pretty new to web development, so don't trust anything in here to
be secure. I have done my best, but I make no guarantees.

https://damyanon.net/flask-series-security/

Password Storage
----------------

Don't store passwords.

https://www.youtube.com/watch?v=8ZtInClXe1Q

Let sign-in with Google/Linked-In/Facebook do the work for you.

SQL Injection
-------------

To prevent SQL injection, this application uses SQLAlchemy to interface
with the database. It has features to prevent SQL injection. Don't use
raw SQL queries to interact with the database and you should be fine.

CSRF Protection
---------------

To prevent CSRF attacks, random string 'tokens' can be placed into forms.
This skeleton uses WTForms for all of its form building, and has the
option to protect against CSRF by generating and including that token.
See: https://flask-wtf.readthedocs.io/en/latest/csrf.html

Cross Site Scripting (XSS)
--------------------------

Flask uses the Jinja2 templating engine by default, and has it set up
to prevent XSS by auto-escaping everything that it inserts into the
page. There are still a few ways to be attacked from this, so be
uber-cautious when handling anything the user provides.

