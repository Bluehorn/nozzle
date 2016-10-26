from coffee.pump import Pump


class Thermosiphon(Pump):

    def __init__(self, heater):
        self.heater = heater

    def pump(self):
        if self.heater.is_hot():
            print("=> => pumping => =>")
