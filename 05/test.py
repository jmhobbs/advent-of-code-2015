from nicestring import has_vowels, has_double, has_no_naughty, is_nice
import newnicestring


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


def test_non_overlapping_doubles():
    # It contains a pair of any two letters that appears at least twice in the
    # string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    # aaa (aa, but it overlaps).
    assert True == newnicestring.has_non_overlapping_doubles("xyxy")
    assert True == newnicestring.has_non_overlapping_doubles("ddbcddefgh")


def test_overlapping_doubles():
    # It contains a pair of any two letters that appears at least twice in the
    # string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    # aaa (aa, but it overlaps).
    assert False == newnicestring.has_non_overlapping_doubles("aaa")
    assert False == newnicestring.has_non_overlapping_doubles("bbbcdefgh")


def test_spaced_repeat():
    # It contains at least one letter which repeats with exactly one letter
    # between them, like xyx, abcdefeghi (efe), or even aaa.
    assert True == newnicestring.has_spaced_repeat("xyx")
    assert True == newnicestring.has_spaced_repeat("abcdefeghi")
    assert True == newnicestring.has_spaced_repeat("aaa")
    assert True == newnicestring.has_spaced_repeat("bcdefgf")


def test_no_spaced_repeat():
    assert False == newnicestring.has_spaced_repeat("abcdefggh")


def test_new_nice():
    # qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    assert True == newnicestring.is_nice("qjhvhtzxzqqjkmpb")
    # xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    assert True == newnicestring.is_nice("xxyxx")


def test_new_naughty():
    # uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    assert False == newnicestring.is_nice("uurcxstgmygtbstg")
    # ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
    assert False == newnicestring.is_nice("ieodomkazucvgmuy")
