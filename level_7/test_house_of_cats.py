import pytest


def house_of_cats(legs):
    """There are some people and cats in a house. You are given the number of legs they have all together. Your task
    is to return an array containing every possible number of people that could be in the house sorted in ascending
    order. It's guaranteed that each person has 2 legs and each cat has 4 legs."""
    for i in range(2, legs + 1):
        return list(range((legs - legs // 4 * 4) // 2, legs // 2 + 1, 2))


@pytest.mark.parametrize('legs, expected', [
    (2, [1]),
    (8, [0, 2, 4]),
    (4, [0, 2]),
    (44, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])])
def test_solution(legs, expected):
    assert house_of_cats(legs) == expected
