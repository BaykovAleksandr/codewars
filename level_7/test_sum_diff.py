import math
import pytest


def sum_differences(pairs):
    """In this kata you need to create a function that takes a 2D array/list of non-negative integer pairs and
    returns the sum of all the "saving" that you can have getting the LCM of each couple of number compared to their
    simple product."""
    prod = []
    lcm = []
    for pair in pairs:
        prod.append(pair[0] * pair[1])
        lcm.append(math.lcm(*pair))
    return sum([a - b for a, b in zip(prod, lcm)])


@pytest.mark.parametrize('lst, expected', [
    ([[15, 18], [4, 5], [12, 60]], 840),
    ([[1, 1], [0, 0], [13, 91]], 1092),
    ([[15, 7], [4, 5], [19, 60]], 0),
    ([], 0)])
def test_solution(lst, expected):
    assert sum_differences(lst) == expected
