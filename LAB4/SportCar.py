from Car import Car
from Engine import Engine
from Driver import Driver

class SportCar(Car):
    speed: int
    def __init__(self, MarkType: str, ClassType: str, weight: int,driver: Driver, motor: Engine, speed: int):
        super().__init__(MarkType, ClassType, weight, driver, motor)
        self.speed = speed
    def __str__(self):
        return super().__str__()  + " " + str(self.speed)