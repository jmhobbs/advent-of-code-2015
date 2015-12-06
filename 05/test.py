from nicestring import has_vowels


def test_has_vowels():
    assert True == has_vowels("ababa", 3)
    assert True == has_vowels("baeioub", 5)


def test_has_insufficient_vowels():
    assert False == has_vowels("abcd", 3)


def test_has_no_vowels():
    assert False == has_vowels("bcdfghjklm")
