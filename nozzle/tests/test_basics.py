# -*- coding: utf-8 -*-

"""
Illustrates and tests the most basic uses of an IOC container.
"""

from nozzle.injector import Injector
from nozzle import annotations


def test_basic_injection():
    injector = Injector()
    some_service = injector.build(SomeService)
    assert isinstance(some_service, SomeService)
    assert isinstance(some_service.sessionmaker, SessionMaker)
    assert isinstance(some_service.memory_cache, MemoryCache)


class DatabaseEngine(object):
    pass


class MemoryCache(object):
    pass


class SessionMaker(object):
    @annotations.inject(engine=DatabaseEngine)
    def __init__(self, engine):
        """
        :param DatabaseEngine engine: Configuration of database
        """
        self.engine = engine


class SomeService(object):
    @annotations.inject(sessionmaker=SessionMaker,
                        memory_cache=MemoryCache)
    def __init__(self, sessionmaker, memory_cache):
        """
        :param SessionMaker sessionmaker: Factory for ORM sessions
        :param MemoryCache memory_cache: Service for caching replies
        """
        self.sessionmaker = sessionmaker
        self.memory_cache = memory_cache
