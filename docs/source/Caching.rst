Caching Design
===============

In order to reduce the load on the server, the application supports
caching via the flask-cache extension. This extension stores the result
of a certain template render, allowing the server to bypass re-rendering
it for the next call.

The syntax is to decorate views with ```@cache.cached(timeout=time)```
where time is an integer denoting the number of seconds that the cached
version is valid. 60 seconds would be a reasonable default.
