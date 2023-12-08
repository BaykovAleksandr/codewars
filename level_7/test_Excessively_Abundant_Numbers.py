import pytest


def abundant_number(num):
    """An abundant number or excessive number is a number for which the sum of its proper divisors is greater than
    the number itself.
The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12)."""

    a = [i for i in range(1, num) if num % i == 0]

    return True if sum(a) > num else False


@pytest.mark.parametrize('num, expected', [(18, True), (12, True),
                                           (37, False), (120, True), (77, False), (118, False), (11690, True)
                                           ])
def test_solution(num, expected):
    assert abundant_number(num) == expected
