import pytest


def reverse_middle(lst):
    """Write a function that takes a list of at least four elements as an argument and returns a list of the middle
    two or three elements in reverse order."""
    if len(lst) % 2:

        return list(reversed(lst[len(lst) // 2 - 1:len(lst) // 2 + 2]))

    else:

        return list(reversed(lst[len(lst) // 2 - 1:len(lst) // 2 + 1]))


@pytest.mark.parametrize('lst, expected', [
    ([1, False, 'string', {}, 7.43], [{}, 'string', False]),
    ([4, 3, 100, 1], [100, 3])])
def test_solution(lst, expected):
    assert reverse_middle(lst) == expected
