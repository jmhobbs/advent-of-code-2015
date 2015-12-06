from nicestring import has_vowels, has_double, has_no_naughty, is_nice


def test_has_vowels():
    assert True == has_vowels("ababa", 3)
    assert True == has_vowels("baeioub", 5)


def test_has_insufficient_vowels():
    assert False == has_vowels("abcd", 3)


def test_has_no_vowels():
    assert False == has_vowels("bcdfghjklm")


def test_has_doubles():
    assert True == has_double("hjkklm")
    assert True == has_double("hhjlm")
    assert True == has_double("hjklmm")


def test_has_no_doubles():
    assert False == has_double("hjklm")


def test_has_no_naughty():
    assert True == has_no_naughty("acefghpx")


def test_has_naughty():
    assert False == has_no_naughty("abcdefg")
    assert False == has_no_naughty("acdefg")
    assert False == has_no_naughty("acepqfg")
    assert False == has_no_naughty("acepfgxy")


def test_nice():
    # ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    # aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    assert True == is_nice("ugknbfddgicrmopn")
    assert True == is_nice("aaa")


def test_naughty():
    # jchzalrnumimnmhp is naughty because it has no double letter.
    # haegwjzuvuyypxyu is naughty because it contains the string xy.
    # dvszwmarrgswjxmb is naughty because it contains only one vowel.
    assert False == is_nice("jchzalrnumimnmhp")
    assert False == is_nice("haegwjzuvuyypxyu")
    assert False == is_nice("dvszwmarrgswjxmb")
