"""Beecrowd | 2465"""

def search_next_step(matrix: list[list[int]], position: tuple[int], visited: list[tuple[int]], to_visit: list[tuple[int]]) -> None:
    top = (position[0] - 1, position[1]) if position[0] - 1 > -1 else None
    left = (position[0], position[1] - 1) if position[1] - 1 > -1 else None
    bottom = (position[0] + 1, position[1]) if position[0] + 1 < len(matrix) else None
    right = (position[0], position[1] + 1) if position[1] + 1 < len(matrix[0]) else None

    iteration = [i for i in (top, left, bottom, right) if i is not None]

    for (i, j) in iteration:
        if (i, j) not in visited and (i, j) not in to_visit and matrix[i][j] >= matrix[position[0]][position[1]]:
            to_visit.append((i, j))

    visited.append(position)


n = int(input())
x_coord, y_coord = (int(x) for x in input().split())
x_coord, y_coord = x_coord - 1, y_coord - 1

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])

initial_position = (x_coord, y_coord)
to_visit = [initial_position]
visited = []

while len(to_visit) > 0:
    position = to_visit.pop(0)
    search_next_step(matrix, position, visited, to_visit)

print(len(visited))
