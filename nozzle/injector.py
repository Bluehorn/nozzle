# -*- coding: utf-8 -*-

from nozzle.annotations import NOZZLE_ANNOTATIONS_KEY, Key


class Injector(object):

    def __init__(self):
        # Having just the type as the value will not suffice, this needs to
        # be some kind of provider encoding scope and method of creation.

        self._bindings = {}  # dict[Key, type]


    def bind(self, abstraction, concretion):
        """
        Tell the injector to provide `concretion` as the implementation of
        `abstraction` when requested as dependency.

        .. note::

            Probably it is a bad idea to have a bind method here, because the
            injector should not change behaviour after configuration. I guess
            this is the reason why the containers I know separate the binding
            from the injector itself.

        :param type abstraction: Abstraction to bind
        :param type concretion: Concretion to use for abstraction
        """
        self._bindings[Key.make(abstraction)] = concretion

    def build(self, requested_type):
        """
        Build an instance of the requested type and return it.

        :param type requested_type: Type of the object to build
        """
        key = Key.make(requested_type)
        injections = self._find_injections(key)
        kwargs = {name: self.build(self._find_provider(key)) for (name, key) in injections.items()}
        return key.requested_type(**kwargs)

    @staticmethod
    def _find_injections(key):
        # Held in an extra method to be able to select different sources for annotation information, like
        # gathering from Python 3 type hints.
        annotations = getattr(key.requested_type.__init__, NOZZLE_ANNOTATIONS_KEY, None)
        return annotations.get_injections() if annotations else {}

    def _find_provider(self, key):
        """
        Given a key find out the provider (currently the concrete type to use).

        :param Key key: Dependency to look up
        :rtype: type
        :return: Concrete type to use
        """
        return self._bindings.get(key, key.requested_type)
