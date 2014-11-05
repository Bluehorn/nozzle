Injection and decorators
========================

Mixing decorators with injection will usually not work too well. Consider
this example:

.. doctest::

    >>> import functools
    >>> def identity_decorator(f):
    ...     """Basic decorator, here without any functionality."""
    ...     @functools.wraps(f)
    ...     def wrapper(*args, **kwargs):
    ...         return f(*args, **kwargs)
    ...     return wrapper

    >>> from injector import Injector, inject
    >>> class Cache(object):
    ...     pass
    >>> class WebService(object):
    ...     @inject(cache=Cache)
    ...     @identity_decorator
    ...     def __init__(self, cache):
    ...         self.cache = cache

    >>> import inspect
    >>> inspect.getargspec(WebService.__init__)
    ArgSpec(args=[], varargs='args', keywords='kwargs', defaults=None)

    >>> injector = Injector()
    >>> injector.get(WebService)
    Traceback (most recent call last):
      ...
    TypeError: __init__() takes exactly 2 arguments (1 given)

By applying the ``identity_decorator``, the signature of the ``__init__`` method
is lost. Because of this, the injection fails because the name is not found.

nozzle should work in this case, passing the ``cache`` argument into the
``kwargs`` dict. But in the general case this could lead to problems.

If the decorator preserves the signature though, this should just work. So
a solution would be to use the `decorator package`_. Using the decorator
package adds a lot of overhead for calls going through the decorator. It would
be an interesting task to devise a solution that keeps the signature without
adding this overhead. Basic idea: rewrite the example decorator above into this::

    >>> @functools.wraps(f)
    ... def wrapper(self, cache):
    ...     args = (cache,)
    ...     kwargs = {}
    ...     return f(*args, **kwargs)

This can only be done by modifying the byte code of the wrapper function or
adding an extra redirection (like decorator is doing).

.. _decorator package: https://pypi.python.org/pypi/decorator
