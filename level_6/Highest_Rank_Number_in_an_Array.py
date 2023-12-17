import pytest


def highest_rank(arr):
    """Complete the method which returns the number which is most frequent in the given input array. If there is a
    tie for most frequent number, return the largest number among them. Note: no empty arrays will be given."""
    counts = {x: arr.count(x) for x in arr}
    res = {key: value for key, value in sorted(counts.items(), key=lambda item: (-item[1], -item[0]))}
    for i in range(1):
        for key in res.keys():
            return key


@pytest.mark.parametrize('arr, expected',
                         [([12, 10, 8, 12, 7, 6, 4, 10, 12], 12),
                          ([12, 10, 8, 12, 7, 6, 4, 10, 10], 10),
                          ([12, 10, 8, 12, 7, 6, 4, 10, 12, 10], 12),
                          ([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10], 3),
                          ([1, 2, 3], 3)])
def test_solution(arr, expected):
    assert highest_rank(arr) == expected
