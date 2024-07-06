"""Beecrowd | 2260"""

test_cases = int(input())

for i in range(test_cases):
    dice = []
    for i in range(3):
        dice += [int(x) for x in input().split(' ')]
    if (
        (dice[0] + dice[5] == dice[1] + dice[3] == dice[2] + dice[4] == 7)
        and (sorted(dice) == [1, 2, 3, 4, 5, 6])
    ):
        print('SIM')
    else:
        print('NAO')
