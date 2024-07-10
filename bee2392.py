"""Beecrowd | 2392"""

rocks, frogs = (int(x) for x in input().split(' '))
bitmap = [0 for _ in range(rocks)]
for i in range(frogs):
    position, jump = (int(x) for x in input().split(' '))
    for i_rock in range(1, position):
        if (position - i_rock) % jump == 0:
            bitmap[i_rock - 1] = 1
    for i_rock in range(position, rocks + 1):
        if (i_rock - position) % jump == 0:
            bitmap[i_rock - 1] = 1

for n in bitmap:
    print(n)
