"""Beecrowd | 2409"""


def passa_colchao(a, b, c, h, l):
    passa = False
    if (
        (a <= h and b <= l) or (a <= l and b <= h) or (b <= l and c <= h)
        or (b <= h and c <= l) or (c <= h and a <= l) or (c <= l and a <= h)
    ):
        passa = True
    return passa


a, b, c = [int(x) for x in input().split()]
h, l = [int(x) for x in input().split()]
PASSA = passa_colchao(a, b, c, h, l)

print('S' if PASSA else 'N')
