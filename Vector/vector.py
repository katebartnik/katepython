class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x*other, self.y*other)
        return self.x*other.y + self.y*other.x

    def __eq__(self, other):
        return self.x == other.x  and self.y == other.y

    def __gt__(self, other):
        return self.length > other.length

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** (0.5)

# v1 = Vector(1,2)
# v2 = Vector(2,3)
# v3 = Vector(3,3)
# print(v1+v2+v3)