"""Beecrowd | 1087"""

while True:
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 == 0 and x2 == 0 and x2 == 0 and y2 == 0:
        break
    else:
        diff_x_y = x1 - y1
        sum_x_y = x1 + y1
        if x1 == x2 and y1 == y2:
            print(0)
        elif x1 == x2 or y1 == y2 or x2 - y2 == diff_x_y or x2 + y2 == sum_x_y:
            print(1)
        else:
            print(2)
