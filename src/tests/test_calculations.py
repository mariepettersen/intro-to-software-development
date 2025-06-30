def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

from geo_calculator.calculations import find_average

def test_find_average():
    test_case = [1, 2, 3, 4, 5, 6]
    assert find_average(test_case) == 3.5  