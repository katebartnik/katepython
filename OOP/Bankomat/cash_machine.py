class CashMachine:
    is available = False

    @property
    def is_avaiable(self):
        if len(self._money) == 0:
            return False
        return True

    def put_money(self, bills):
        self.bills = bills

    def withdraw_money(self, amount):
        if self.is_avaiable:
            return self.bills
        return []
