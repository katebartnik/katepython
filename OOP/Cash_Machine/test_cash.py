def test_cash_machine_not_avaiable:
    cm = CashMachine()
    assert cm.is_avaiable is False

def test_cash_machine_put_money:
    cm = CashMachine()
    cm.put_money ([50])
    assert cm.put_money

