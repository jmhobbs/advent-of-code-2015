
total = 0

with open('input.txt', 'rb') as handle:
    for line in handle:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)

        s1 = 2*l*w
        s2 = 2*w*h
        s3 = 2*h*l

        d = s1 + s2 + s3 + (min(s1, min(s2, s3)) / 2)

        total += d

print total
