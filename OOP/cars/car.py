class ElectricCar:
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