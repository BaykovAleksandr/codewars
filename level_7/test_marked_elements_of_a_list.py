import pytest


def remover(integer_list, values_list):
    """Define a method/function that removes from a given array of integers all the values contained in a second
    array."""
    inter_res = list(set(integer_list).difference(values_list))
    final = []
    for i in integer_list:
        if i in inter_res:
            final.append(i)
    return final


@pytest.mark.parametrize('int_list, value_list, expected', [
    ([1, 1, 2, 3, 1, 2, 3, 4], [1, 3], [2, 2, 4]),
    ([1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2], [5, 6, 7, 8]),
    ([8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3], [8, 7, 6, 5, 1]),
    ([4, 4, 2, 3], [2, 2, 4, 3], [])]
                         )
def test_solution(int_list, value_list, expected):
    assert remover(int_list, value_list) == expected
