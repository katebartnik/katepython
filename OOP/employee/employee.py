class Employee:

    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self.__registered_hours = 0

    def register_time(self, time):
        self.__registered_hours = time

    def pay_salary(self):
        if self.__registered_hours <= 8:
            to_pay = self.__registered_hours * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.__registered_hours - 8) * self.rate_per_hour * 2
        self.__registered_hours = 0
        return to_pay

emp = Employee("Jan","Kowalski", 200)
print(emp._Employee__registered_hours)
emp._Employee__registered_hours = 10
print(emp.pay_salary())