import pytest


def solution(line):
    """Complete the solution so that the function will break up camel casing, using a space between words."""
    return ''.join(i if i.islower() else ' ' + i for i in line)


@pytest.mark.parametrize('line, result', [("helloWorld", "hello World"),
                                          ("camelCase", "camel Case"),
                                          ("breakCamelCase", "break Camel Case")])
def test_solution(line, result):
    assert solution(line) == result
