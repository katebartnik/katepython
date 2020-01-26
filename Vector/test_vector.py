from vector import Vector


class TestVector:

    def test_create(self):
        v = Vector(x=1, y=2)
        assert True

    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 2)
        v3 = Vector(3, 4)
        v = v1 + v2
        assert v.x == 3
        assert v.y == 4
        assert v == v3

    def test_sub(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 2)
        v3 = Vector(-1, 0)
        assert v1 - v2 == v3

    def test_multiply_by_other_vector(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 2)
        assert v1 * v2 == 6

    def test_multiply_by_int(self):
        v = Vector(3, 4)
        assert v * 3 == Vector(9, 12)

    def test_length(self):
        v = Vector(3, 4)
        assert v.length == 5

    def test_greater_than(self):
        v1 = Vector(1, 1)
        v2 = Vector(2, 2)
        assert v2 > v1
        assert v1 < v2