from employee import Employee, PremiumEmployee, AmountBonus, PercentBonus

class TestEmployee:

    def test_init(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e._registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.rate_per_hour == 100
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200


class TestPremiumEmployee:

    def test_init(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e._registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        assert e.rate_per_hour == 100
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        bonus = AmountBonus(1000)
        e.give_bonus(bonus)
        assert e.bonuses == [bonus]

    def test_pay_salary_normal_hours_amount_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        bonus = AmountBonus(1000)
        e.give_bonus(bonus)
        assert e.pay_salary() == 1500

    def test_pay_salary_with_over_hours_amount_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(10)
        e.give_bonus(AmountBonus(1000))
        assert e.pay_salary() == 2200
        assert e.pay_salary() == 0

    def test_pay_salary_normal_hours_percent_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        bonus = PercentBonus(10)
        e.give_bonus(bonus)
        assert e.pay_salary() == 550

    def test_pay_salary_normal_hours_2_percent_bonuses(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        bonus1 = PercentBonus(10)
        bonus2 = PercentBonus(10)
        e.give_bonus(bonus1)
        e.give_bonus(bonus2)
        assert e.pay_salary() == 600