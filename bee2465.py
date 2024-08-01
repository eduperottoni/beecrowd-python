"""Beecrowd | 2465"""

def search_next_step(matrix: list[list[int]], position: tuple[int], visited: list[tuple[int]]) -> tuple[int]:
    top = (position[0] - 1, position[1]) if position[0] - 1 > -1 else None
    left = (position[0], position[1] - 1) if position[1] - 1 > -1 else None
    bottom = (position[0] + 1, position[1]) if position[0] + 1 < len(matrix) else None
    right = (position[0], position[1] + 1) if position[1] + 1 < len(matrix[0]) else None

    iteration = [i for i in (top, left, bottom, right) if i is not None]

    for (i, j) in iteration:
        if (i, j) not in visited and matrix[i][j]:
            return (i, j)

    return (None, None)


n = int(input())
x_coord, y_coord = (int(x) for x in input().split())
x_coord, y_coord = x_coord - 1, y_coord - 1

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

flags_up = 0
initial_position = (x_coord, y_coord)

# Cada nodo deve ter a referência de quem o passou e para onde está apontando

# Cada aluno dever executar esse loop 
for i in ['r', 'b', 'l', 't']:
    