import pytest


def t_area(t_str):
    """Calculate area of given triangle. Create a function t_area that will take a string which will represent triangle,
     find area of the triangle, one space will be equal to one length unit. The smallest triangle will have one length
     unit."""

    return (t_str.split("\n")[-2].count(".") - 1) ** 2 / 2


@pytest.mark.parametrize('triangle, expected', [('\n.\n. .\n', 0.5), ('\n.\n. .\n. . .\n. . . .\n. . . . .\n', 8.0),
                                                ('\n.\n. .\n. . .\n', 2.0), (
                                                        '\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . '
                                                        '.\n. . . . . . . .\n. . . . . . . . .\n',
                                                        32.0)
                                                ])
def test_solution(triangle, expected):
    assert t_area(triangle) == expected
