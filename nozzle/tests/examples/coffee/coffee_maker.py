# -*- coding: utf-8 -*-

from nozzle.annotations import inject
from nozzle.generics.lazy import Lazy

from coffee.heater import Heater
from coffee.pump import Pump


class CoffeeMaker(object):

    @inject(heater=Lazy[Heater], pump=Pump)
    def __init__(self, heater, pump):
        self.heater = heater
        self.pump = pump

    def brew(self):
        self.heater.get().on()
        self.pump.pump()
        print("[_]P coffee! [_]P")
        self.heater.get().off()
