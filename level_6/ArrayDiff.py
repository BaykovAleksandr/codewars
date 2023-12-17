import pytest


def array_diff(a, b):
    """Your goal in this kata is to implement a difference function, which subtracts one list from another and
    returns the result. It should remove all values from list a, which are present in list b keeping their order."""
    for num in b:
        while num in a:
            a.remove(num)
    return a


@pytest.mark.parametrize('lst_a, lst_b, expected', [([1, 2], [1], [2]),
                                                    ([1, 2, 2], [1], [2, 2]),
                                                    ([1, 2, 2], [2], [1]),
                                                    ([1, 2, 2], [], [1, 2, 2]),
                                                    ([], [1, 2], []),
                                                    ([1, 2, 3], [1, 2], [3])])
def test_solution(lst_a, lst_b, expected):
    assert array_diff(lst_a, lst_b) == expected
