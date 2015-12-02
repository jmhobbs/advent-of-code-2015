
total = 0

with open('input.txt', 'rb') as handle:
    for line in handle:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)

        dim = sorted([l, w, h])

        length = dim[0]*2 + dim[1]*2 + l * w * h

        total += length

print total
