# -*- coding: utf-8 -*-

from nozzle.injector import Injector
from coffee.coffee_maker import CoffeeMaker


def main():
    injector = Injector()
    coffee_maker = injector.build(CoffeeMaker)
    coffee_maker.brew()


if __name__ == "__main__":
    main()
