"""Beecrowd | 2139"""

# Para cada coordenada, o valor pode ser definido pela
# diferença entre a coordenada e a posição do soco
test_cases = int(input())

for t in range(test_cases):
    lines, columns, y_punch, x_punch = (int(x) for x in input().split())
    y_punch, x_punch = y_punch - 1, x_punch - 1

    wall = []

    for line in range(lines):
        wall.append([int(x) for x in input().split()])

    for i_line, i in enumerate(wall):
        for j_col, j in enumerate(i):
            diff_line = y_punch - i_line
            diff_column = x_punch - j_col
            to_sum = 10 - max(abs(diff_line), abs(diff_column))
            wall[i_line][j_col] = wall[i_line][j_col] + (to_sum if to_sum > 0 else 1)

    print(f'Parede {t + 1}:')
    for i in wall:
        print(str(i)
              .replace('[', '')
              .replace(']', '')
              .replace(', ', ' '))
