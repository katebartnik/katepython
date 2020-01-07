from car import ElectricCar

def test_electric_car_init():
    ec = ElectricCar(100)
    assert ec._ElectricCar__max_range == 100

def test_electric_car_drice_below_max_range():
    ec = ElectricCar(100)
    assert ec.drive(70) == 70

def test_electric_car_drice_below_over_max_range_in_to_drives():
    ec = ElectricCar(100)
    assert ec.drive(70) == 70
    assert ec.drive(50) == 30
    assert ec.drive(50) == 0

def test_electric_car_charge():
    ec = ElectricCar(100)
    assert ec.drive(70) == 70
    assert ec.drive(50) == 30
    assert ec.drive(50) == 0
    ec.charge()
    assert ec.drive(50) == 50