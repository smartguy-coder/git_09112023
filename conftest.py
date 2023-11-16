import pytest

from oop_library import Account


@pytest.fixture
def account() -> Account:
    bank_account = Account(owner="Petro", address="Lvivska str, 18")
    return bank_account
