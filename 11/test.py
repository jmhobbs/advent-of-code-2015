from pswd import ElfPasswordCheck, SantaPasswordGenerator


def test_invalid():
    # hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    assert False == ElfPasswordCheck("hijklmmn")
    # abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    assert False == ElfPasswordCheck("abbceffg")
    # abbcegjk fails the third requirement, because it only has one double letter (bb).
    assert False == ElfPasswordCheck("abbcegjk")
    assert False == ElfPasswordCheck("abbbcd")


def test_valid():
    # The next password after abcdefgh is abcdffaa.
    assert True == ElfPasswordCheck("abcdffaa")
    # The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
    assert True == ElfPasswordCheck("ghjaabcc")


def test_edge_cases():
    assert True == ElfPasswordCheck("aadccxyz")

def test_iteration():
    # xx, xy, xz, ya, yb
    spg = SantaPasswordGenerator("xx")
    assert "xy" == spg.iterate()
    assert "xz" == spg.iterate()
    assert "ya" == spg.iterate()
    assert "yb" == spg.iterate()

    spg = SantaPasswordGenerator("azz")
    assert "baa" == spg.iterate()
