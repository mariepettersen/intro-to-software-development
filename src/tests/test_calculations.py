import pytest

def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

from geo_calculator.calculations import find_average

def test_find_average():
    test_case = [1, 2, 3, 4, 5, 6]
    assert find_average(test_case) == 3.5  

from geo_calculator.calculations import gardners_equation

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density, rel=1e-7)
