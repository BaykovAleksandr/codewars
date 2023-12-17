import pytest
from string import ascii_lowercase as al


def is_pangram(s):
    """A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
    "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is
    irrelevant).
    Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
    punctuation."""
    a = set(ch for ch in s.lower())
    return True if set(al).issubset(a) else False


@pytest.mark.parametrize('text, result', [("The quick, brown fox jumps over the lazy dog!", True),
                        ("1bcdefghijklmnopqrstuvwxyz", False)]
                         )
def test_solution(text, result):
    assert is_pangram(text) == result
