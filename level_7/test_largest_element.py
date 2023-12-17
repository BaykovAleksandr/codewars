import pytest


def largest(n, xs):
    """Write a program that outputs the top n elements from a list."""
    return sorted(xs)[-n:] if n else []


@pytest.mark.parametrize('num, lst, expected', [(2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 10]),
                                                (3, [5, 1, 5, 2, 3, 1, 2, 3, 5], [5, 5, 5]),
                                                (7, [9, 1, 50, 22, 3, 13, 2, 63, 5], [3, 5, 9, 13, 22, 50, 63])])
def test_solution(num, lst, expected):
    assert largest(num, lst) == expected
