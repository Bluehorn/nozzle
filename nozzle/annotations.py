# -*- coding: utf-8 -*-

NOZZLE_ANNOTATIONS_KEY = "_nozzle_"


def inject(**kwargs):
    def decorate(target):
        annotations = getattr(target, NOZZLE_ANNOTATIONS_KEY, None)
        if annotations is None:
            annotations = InjectionAnnotations()
            setattr(target, NOZZLE_ANNOTATIONS_KEY, annotations)
        annotations.add_injections(**kwargs)
        return target
    return decorate


class InjectionAnnotations(object):
    __slots__ = "_injections",

    def __init__(self):
        self._injections = {}

    def __repr__(self):
        return "<InjectionAnnotations {0}>".format(self._injections)

    def get_injections(self):
        return dict(self._injections)

    def add_injections(self, **kwargs):
        for name in kwargs:
            self._injections[name] = Key.make(kwargs[name])


class Key(object):
    __slots__ = "_requested_type",

    def __init__(self, requested_type):
        self._requested_type = requested_type

    def __str__(self):
        return self._requested_type.__name__

    def __repr__(self):
        return "<Key {0}>".format(self._requested_type)

    @property
    def requested_type(self):
        """
        Access the type requested for this injection key.

        :type: type
        """
        return self._requested_type

    @classmethod
    def make(cls, request):
        if isinstance(request, Key):
            return request
        else:
            return Key(request)
