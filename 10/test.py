from looksay import LookAndSay


def test_one_one():
    # 1 becomes 11 (1 copy of digit 1).
    ls = LookAndSay("1")
    assert ls.iterate() == "11"


def test_two_ones():
    # 11 becomes 21 (2 copies of digit 1).
    ls = LookAndSay("11")
    assert ls.iterate() == "21"


def test_one_two_one_one():
    # 21 becomes 1211 (one 2 followed by one 1).
    ls = LookAndSay("21")
    assert ls.iterate() == "1211"


def test_three_ones_two_twos_one():
    # 1211 becomes 111221 (one 1, one 2, and two 1s).
    ls = LookAndSay("1211")
    assert ls.iterate() == "111221"


def test_the_long_one():
    # 111221 becomes 312211 (three 1s, two 2s, and one 1).
    ls = LookAndSay("111221")
    assert ls.iterate() == "312211"
