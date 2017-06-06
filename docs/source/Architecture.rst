Code Architecture
=================

This document details how the code is meant to fit together. It's not
the nitty-gritty details of style, but the overall philosophy of how to
create and arrange code.

Clean Architecture
------------------

A major inspiration of this code is a talk given by Brandon Rhodes on
"The Clean Architecture in Python". It is avaiable on youtube at this
link: https://www.youtube.com/watch?v=DJtef410XaM

To boil it down into a statement though it is:

::

    Separate policy from mechanism by making an imperative shell
    wrapping a functional core.

In human terms, it means that most of your code should be reusable
functions that take in data and return other data, with no side effects
(aka. functional programming style). These functions should not contain
any business logic. When it comes time to actually implement business
logic, do it using high level 'imperative' subroutines that chain
together the low level functions.

For example:

.. code-block:: python

    def find_definition(word):
        """High level imperative subroutine"""
        url = build_search_url(word)
        data = requests.get(url).json()
        return pluck_definition(data)

    def build_search_url(word):
        """Low level functional mechanism"""
        q = 'define' + word
        url = 'http://api.duckduckgo.com/?'
        url += urlencode({'q' : q, 'format' : 'json'})
        return url

Modular Architecture
--------------------

Since this project is meant as a skeleton for future flask applications,
it uses the flask 'blueprint' architecture. This allows different
modules to be dropped in fairly easily.

MVC Design Pattern
------------------

Both the main application and the drop-in modules should conform the MVC
(models-views-controller) design pattern. 'Models' refers to the data
model, which in turn defines the database. 'Views' refers to the front
end of how the user interacts with the site. 'Controller' refers to the
business logic, and facilitates/moderates the user interaction with the
data mode.

The convention for this project is:
    models go in ```models.py``` files
    views go in ```views.py``` files
    controllers go in ```__init__.py``` files
