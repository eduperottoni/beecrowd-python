"""Beecrowd | 2375"""


diameter = int(input())
height, width, depth = [int(x) for x in input().split()]

if height >= diameter and width >= diameter and depth >= diameter:
    print('S')
else:
    print('N')
