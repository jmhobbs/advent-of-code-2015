from pswd import ElfPasswordCheck, SantaPasswordGenerator

# These are slower than the other tests, so I moved them to their own file.


def test_examples():
    # The next password after abcdefgh is abcdffaa.
    spg = SantaPasswordGenerator("abcdefgh")
    while True:
        pwd = spg.iterate()
        if ElfPasswordCheck(pwd):
            assert pwd == "abcdffaa"
            break

    # The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
    spg = SantaPasswordGenerator("ghijklmn")
    while True:
        pwd = spg.iterate()
        if ElfPasswordCheck(pwd):
            assert pwd == "ghjaabcc"
            break
