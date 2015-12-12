from escapestring import EscapedString

with open("input.txt", "rb") as handle:
    total = 0
    for line in handle:
        es = EscapedString(line.rstrip("\n"))
        total += len(es.escape())
        total -= es.code_length
    print total
