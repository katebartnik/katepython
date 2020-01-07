class ElectricCar:
    """Samochód elektryczny"""
    def __init__(self, max_range):
        self.__max_range = max_range
        self.counter = 0

    def drive(self, distance):
        if self.counter + distance < self.__max_range:
            self.counter += distance
            to_travel = distance + 0.1 * distance
        else:
            to_travel = self.__max_range - self.counter
            self.counter = self.__max_range
        return to_travel

    def charge(self):
        self.counter = 0

    @property
    def can_move(self):
        return self.counter < self.__max_range

ec = ElectricCar(100)
ec.drive(100)
print(ec.can_move)