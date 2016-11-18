# -*- coding: utf-8 -*-

"""
Illustrates the most basic ways of binding abstractions to concretions.
"""

from nozzle.injector import Injector
from nozzle import annotations


def test_trivial_binding():
    """
    The core idea of dependency injection is to depend on abstractions and
    work on concrete implementations of these. This example tells the injector
    which concrete implementation of the abstraction to use.
    """
    injector = Injector()
    injector.bind(Abstraction, Concretion)
    injected = injector.build(InjectedClass)
    assert isinstance(injected.dependency, Concretion)


class Abstraction(object):
    pass


class Concretion(Abstraction):
    pass


class InjectedClass(object):
    @annotations.inject(dependency=Abstraction)
    def __init__(self, dependency):
        self.dependency = dependency
