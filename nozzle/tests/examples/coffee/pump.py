from abc import ABCMeta, abstractmethod


class Pump(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def pump(self):
        pass
