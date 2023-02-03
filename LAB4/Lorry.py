from Car import Car
from Engine import Engine
from Driver import Driver


class Lorry(Car):
    carrying: int

    def __init__(self, markType: str, classType: str, weight: int, driver: Driver, motor: Engine, carrying: int):
        super().__init__(markType, classType, weight, driver, motor)
        self.carrying = carrying

    def __str__(self):
        return super().__str__() + " " + str(self.carrying)
