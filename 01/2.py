floor = 0
i = 0
with open("input.txt", 'rb') as handle:
    while True:
        i += 1
        c = handle.read(1)
        if not c:
            print 'EOF', floor
            break
        if '(' == c:
            floor += 1
        elif ')' == c:
            floor += -1
            if floor < 0:
                print 'basement at', i
                break
