__author__ = 'shellyan'

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]


def cycle(a, b, c):
    one = a[:-1]
    one.insert(0, b[0])
    two = [c[0], b[1], a[2]]
    three = c[1:]
    three.append(b[2])
    print one+two+three


cycle(a=[4, 1, 2], b=[7, 5, 3], c=[8, 9, 6])
