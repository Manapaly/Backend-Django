from Engine import Engine
from Driver import Driver


class Car:
    markType: str
    classType: str
    weight: int
    driver: Driver
    motor: Engine

    def __init__(self, MarkType: str, ClassType: str, weight: int, driver: Driver, motor: Engine):
        self.markType = MarkType
        self.classType = ClassType
        self.driver = driver
        self.weight = weight
        self.motor = motor

    def Start(self):
        print("poehali")

    def Stop():
        print("ostanovis beiba")

    def turnLeft(self):
        print("povorot nalevo")

    def turnRigth(self):
        print("povorot napravo")

    def __str__(self):
        return self.markType + " " + self.classType + " " + str(
            self.weight) + " " + self.driver.__str__() + " " + self.motor.__str__()
