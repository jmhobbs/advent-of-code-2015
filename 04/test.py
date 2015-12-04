from adventminer import AdventMiner


def test_case_1_1():
    # If your secret key is abcdef, the answer is 609043, because the MD5 hash
    # of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the
    # lowest such number to do so.

    a = AdventMiner("abcdef")
    n = a.run()

    assert n == 609043


def test_case_1_2():
    # If your secret key is pqrstuv, the lowest number it combines with to make
    # an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
    # pqrstuv1048970 looks like 000006136ef....

    a = AdventMiner("pqrstuv")
    n = a.run()

    assert n == 1048970
