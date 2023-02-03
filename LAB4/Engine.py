class Engine:
    power: str
    manufacture: str
    def __init__(self, power: str, manufacture: str):
        self.power = power
        self.manufacture = manufacture
    def __str__(self):
        return str(self.power) + " " + str(self.manufacture)
    