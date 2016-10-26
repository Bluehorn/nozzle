# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Heater(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def is_hot(self):
        pass
