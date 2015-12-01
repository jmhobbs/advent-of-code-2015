floor = 0

with open("input.txt", 'rb') as handle:
    while True:
        c = handle.read(1)
        if not c:
            print 'EOF', floor
            break
        if '(' == c:
            floor += 1
        elif ')' == c:
            floor += -1
