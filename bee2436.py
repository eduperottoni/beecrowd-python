"""Beecrowd | 2436"""

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


lines, columns = [int(x) for x in input().split()]
start_line, start_column = [int(x) for x in input().split()]

matrix = []
visited = []
for line in range(lines):
    matrix.append([int(x) for x in input().split()])

adjacent = (start_line - 1, start_column - 1)
visited.append(adjacent)

while adjacent != (None, None):
    visited.append(adjacent)
    adjacent = search_next_step(matrix, adjacent, visited)

print(f'{visited[-1][0] + 1} {visited[-1][1] + 1}')
