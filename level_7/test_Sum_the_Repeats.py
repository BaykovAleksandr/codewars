import pytest


def repeat_sum(l):
    """Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers
    that appear in two or more lists in the input list."""

    f = [n for s in l for n in set(s)]
    return sum(n for n in set(f) if f.count(n) > 1)


@pytest.mark.parametrize('lst, expected', [
    ([[1, 2, 3], [2, 8, 9], [7, 123, 8]], 10),
    ([[1], [2], [3, 4, 4, 4], [123456789]], 0),
    ([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]], 9)])
def test_solution(lst, expected):
    assert repeat_sum(lst) == expected
