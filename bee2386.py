"""Beecrowd | 2386"""

width, height, depth, radius = [int(x) for x in input().split()]

diagonal1 = ((width/2)**2 + (height/2)**2)**(1/2)
diagonal2 = ((width/2)**2 + (depth/2)**2)**(1/2)
diagonal3 = ((depth/2)**2 + (height/2)**2)**(1/2)

if diagonal1 <= radius and diagonal2 <= radius and diagonal3 <= radius:
    print('S')
else:
    print('N')
