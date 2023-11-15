def test_create_balance(account):
    assert account.balance == 0


def test_create_add_money(account):
    account.add_money(100)
    print(account.card)
    assert account.balance == 100
