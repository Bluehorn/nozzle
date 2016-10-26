from abc import ABCMeta, abstractmethod


class ElectricHeader(Heater):

    def __init__(self):
        self.heating = False

    def on(self):
        self.heating = True
        print("~ ~ ~ heating ~ ~ ~")

    def off(self):
        self.heating = False

    def is_hot(self):
        return self.heating
