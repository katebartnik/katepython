from vector import Vector

def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(2, 1)

    result = v1 + v2
    assert result.x == 3
    assert result.y == 3

def test_vector_sub():
    v1 = Vector(1, 4)
    v2 = Vector(5, 8)

    result = v1 - v2
    assert result.x == -4
    assert result.y == -5

