"""Beecrowd | 1069"""

for i in range(int(input())):
    caracters = input()
    opened = []
    diamonds_counter = 0
    for c in caracters:
        if c == '<':
            opened.append(c)
        elif c == '>':
            if len(opened) > 0:
                opened.pop(0)
                diamonds_counter += 1

    print(diamonds_counter)
