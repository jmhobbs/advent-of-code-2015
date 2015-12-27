import re


MATCHER = re.compile(r'([A-Za-z]+) would (lose|gain) (\d+) happiness units by sitting next to ([A-Za-z]+).')


def parse_line(line):
    # Alice would lose 2 happiness units by sitting next to Bob.
    mo = MATCHER.match(line)
    points = int(mo.group(3))
    if mo.group(2) == 'lose':
        points = points * -1
    return (mo.group(1), points, mo.group(4))
