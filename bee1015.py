"""Beecrowd | 1015"""

xa, ya = [float(x) for x in input().split()]
xb, yb = [float(x) for x in input().split()]

distance = ((xb-xa)**2 + (yb-ya)**2)**(1/2)

print(f'{distance:.4f}')
