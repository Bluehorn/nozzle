Alternatives to nozzle
======================

You may wonder why I wrote `nozzle` given that there already are a few IOC
containers for Python. I have to admit that I did not like those so far,
which probably translates to NIH syndrome.

So here is my take why I do not like those alternatives:


injector
--------

:Homepage: https://github.com/alecthomas/injector

This does not look too bad, but there is one show stopper: Every instance
configured by the container retains a reference to the IOC container itself
as :code:`instance.__injector__`. This looks like a guaranteed memory leak to
me or at least like it will cause a lot of otherwise unneccessary GC cycles.


snake-guice
-----------

:Homepage: https://code.google.com/p/snake-guice/

Seems to be dead since end of 2012. Also add too much Java-like boilerplate.
I think there must be a more pythonic way to do this.


pinject
-------

:Homepage: https://github.com/google/pinject

`pinject` resolves dependencies solely based on the parameter name, not unlike
what :file:`py.test` does for fixtures. I find it too hard to find the
relevant class given just a name that is also translated from `snake_case` to
`CapitalizedWords`. I'd rather have the name of the class right there so that
I can follow the link in the IDE.

Also, to be discoverable by the injector, all implementations must have been
imported. So this does not work with `pinject`:

**demo.py** ::

    import pinject

    class Builder(object):
        def __init__(self, download_cache):
            self.download_cache = download_cache

    obj_graph = pinject.new_object_graph()
    obj_graph.provide(Builder)

**cache.py** ::

    class DownloadCache(object):
        pass

If you add :code:`import cache` to :file:`demo.py`, this suddenly works but
every IDE under the sun will suggest to remove that "unneeded" import. I'd
prefer to either write ::

    from cache import DownloadCache

    class Builder(object):
        @inject(download_cache=DownloadCache)
        def __init__(self, download_cache):
            ...

which forces the import as it is actually used in the code or, alternatively ::

    class Builder(object):
        @inject(download_cache="cache.DownloadCache")
        def __init__(self, download_cache):
            ...

which does not force the import (as by providing another `DownloadCache`
implementation the import would be superfluous anyway) but allows the injector
to import the basic implementation as a fallback if nobody registered a
better one.
