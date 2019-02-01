""" unit tests for the calculator functions"""


import citest


class TestCalculator:

    def test_addition(self):
        assert 4 == citest.add_numbers(2, 2)

    def test_subtraction(self):
        assert 5 == citest.subtract_numbers(6, 1)