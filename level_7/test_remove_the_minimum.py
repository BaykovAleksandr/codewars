import pytest


def remove_smallest(numbers):
    """Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are
    multiple elements with the same value, remove the one with a lower index. If you get an empty array/list,
    return an empty array/list. Don't change the order of the elements that are left."""
    if not numbers:
        return []
    else:
        b = min(numbers)
        a = numbers[:]
        a.remove(b)
        return a


@pytest.mark.parametrize('lst, expected', [
    ([1, 2, 3, 4, 5], [2, 3, 4, 5]),
    ([5, 3, 2, 1, 4], [5, 3, 2, 4]),
    ([1, 2, 3, 1, 1], [2, 3, 1, 1]),
    ([], [])])
def test_solution(lst, expected):
    assert remove_smallest(lst) == expected
