from nicestring import is_nice

nice_strings = 0
with open("input.txt", "rb") as handle:
    for string in handle:
        nice_strings += 1 if is_nice(string) else 0

print "Found %d Nice Strings" % nice_strings
