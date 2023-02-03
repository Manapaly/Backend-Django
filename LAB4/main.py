from Car import Car
from Lorry import Lorry
from Engine import Engine
from Driver import Driver
from SportCar import SportCar

d1 = Driver('Ernat', 'Manapaly', 2.4)
print(d1)
e1 = Engine(200, 'emmsms')
print(e1)

c1 = Car('mers', 'sedan', 1000, d1, e1)
# self, MarkType: str, ClassType: str, weight: int,driver: Driver, motor: Engine
c2 = Lorry('mers', 'sedan', 1000, d1, e1, 5000)
print(c2)
# self, MarkType: str, ClassType: str, weight: int,driver: Driver, motor: Engine, carrying: int
# self, MarkType: str, ClassType: str, weight: int,driver: Driver, motor: Engine, speed: int
c3 = SportCar('mers', 'sedan', 1000, d1, e1, 300)
c2.Start()
c3.turnLeft()
print(c3)
