"""Beecrowd | 1187"""

operation = input()

total = 0

for i in range(12):
    for j in range(12):
        cell = float(input())
        if 11 - i > j > i:
            total += cell

if operation == "S":
    print(f'{total:.1f}')
else:
    print(f'{total/30:.1f}')
