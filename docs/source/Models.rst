Models Design
=============

The overall architecture uses an MVC (models-views-controller) style, so
data models get their own models.py file. Data models aren't as easy to
modularize though, since you're generally dealing with a single database
with many interconnected tables. For this reason, a single app/models.py
file is included.

It is possible to add to the data model using models.py files in
blueprints by inheriting the abstract 'ModelTable' class from
app/models.py. It is only advisable if the data from the blueprint doesn't
interact with other blueprints. Otherwise you'll have multiple different
ORM classes interacting with a single table, and that violates the
general principle of DRY - don't repeat yourself.