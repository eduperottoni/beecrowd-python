"""Beecrowd | 1366"""

while True:
    n = int(input())

    if n == 0:
        break

    pairs = 0
    for _ in range(n):
        pairs += int(int(input().split(' ')[1]) / 2)

    print(int(pairs / 2))
