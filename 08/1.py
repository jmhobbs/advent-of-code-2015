from escapestring import EscapedString

with open("input.txt", "rb") as handle:
    total = 0
    for line in handle:
        es = EscapedString(line.rstrip("\n"))
        total += es.code_length
        total -= es.string_length
    print total
