Debugging
=========

Preface: Do not allow debug mode to be enabled on a public website. It can
allow arbritrary code execution, so people can 0wn you.

This application includes an extension called flask-debugtools that injects
a cool debug toolbar into your website. It is only active when the app
debug mode is on (see the config.py file).

Supplementary steps are taken to disable caching so that changes can be
viewed immediately.