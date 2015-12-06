
def is_nice(string):
    return has_non_overlapping_doubles(string) and has_spaced_repeat(string)


def has_non_overlapping_doubles(string):
    # It contains a pair of any two letters that appears at least twice in the
    # string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    # aaa (aa, but it overlaps).
    pair = string[0]
    for i in xrange(1, len(string)):
        pair = pair[-1:] + string[i]
        if pair in string[i+1:]:
            return True
    return False


def has_spaced_repeat(string):
    # It contains at least one letter which repeats with exactly one letter
    # between them, like xyx, abcdefeghi (efe), or even aaa.
    for i in xrange(0, len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False
