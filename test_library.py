import pytest

import library


def test_not_can_drive_car():
    result = library.can_drive_car(15)
    assert result is False


def test_can_drive_car():
    result = library.can_drive_car(55)
    assert result is True


def test_not_can_drive_car_min():
    with pytest.raises(ValueError):
        library.can_drive_car(-555)


def test_can_drive_car_max():
    with pytest.raises(ValueError):
        library.can_drive_car(555)
