import pytest


def is_leap_year(year):
    """In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know
    the rules, here they are:

    Years divisible by 4 are leap years,
    but years divisible by 100 are not leap years,
    but years divisible by 400 are leap years."""
    return True if not year % 400 or (not year % 4 and year % 100) else False


@pytest.mark.parametrize('year, expected', [
    (2000, True),
    (2020, True),
    (2015, False),
    (2100, False),
    (2023, False)])
def test_solution(year, expected):
    assert is_leap_year(year) == expected
