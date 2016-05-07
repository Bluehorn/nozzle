# -*- coding: utf-8 -*-

from nozzle.annotations import NOZZLE_ANNOTATIONS_KEY, Key


class Injector(object):

    def build(self, requested_type):
        """
        Build an instance of the requested type and return it.

        :param type requested_type: Type of the object to build
        """
        key = Key.make(requested_type)
        injections = self._find_injections(key)
        kwargs = {name: self.build(key) for (name, key) in injections.items()}
        return key.requested_type(**kwargs)

    @staticmethod
    def _find_injections(key):
        # Held in an extra method to be able to select different sources for annotation information, like
        # gathering from Python 3 type hints.
        annotations = getattr(key.requested_type.__init__, NOZZLE_ANNOTATIONS_KEY, None)
        return annotations.get_injections() if annotations else {}
