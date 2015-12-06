
VOWELS = ('a', 'e', 'i', 'o', 'u')
NAUGHTY_SEQUENCES = ('ab', 'cd', 'pq', 'xy')


def is_nice(string):
    return has_vowels(string) and has_double(string) and has_no_naughty(string)


def has_vowels(string, number=3):
    # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    vowels = filter(None, [c if c in VOWELS else None for c in string])
    return len(vowels) >= number


def has_double(string):
    # It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    c = None
    for ch in string:
        if c == ch:
            return True
        else:
            c = ch
    return False


def has_no_naughty(string):
    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    for naughty in NAUGHTY_SEQUENCES:
        if naughty in string:
            return False
    return True
