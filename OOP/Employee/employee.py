class Bonus:
    def __init__(self, value):
        self.value = value

class AmountBonus(Bonus):
    pass

class PercentBonus(Bonus):
    pass


class Employee:

    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self._registered_hours = 0

    def register_time(self, time):
        self._registered_hours = time

    def pay_salary(self):
        if self._registered_hours <= 8:
            to_pay = self._registered_hours * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self._registered_hours - 8) * self.rate_per_hour * 2
        self._registered_hours = 0
        return to_pay


class PremiumEmployee(Employee):

    def __init__(self, f_name, l_name, rph):
        super().__init__(f_name, l_name, rph)
        self.bonuses = []

    def give_bonus(self, bonus):
        self.bonuses.append(bonus)

    def pay_salary(self):
        to_pay = super().pay_salary()
        amount_bonuses = sum([x.value for x in self.bonuses if isinstance(x, AmountBonus)])
        percent_bonuses = sum([x.value for x in self.bonuses if isinstance(x, PercentBonus)])
        to_pay = to_pay + (to_pay * percent_bonuses) / 100
        to_pay += amount_bonuses
        self.bonuses = []
        return to_pay