"""Beecrowd | 2399"""

table_lenght = int(input())
table_cells = []
for i in range(table_lenght):
    table_cells.append(int(input()))
for i in range(table_lenght):
    if i == 0:
        print(sum(table_cells[:2]))
    elif i == table_lenght - 1:
        print(sum(table_cells[-2:]))
    else:
        print(sum(table_cells[i-1:i+2]))
