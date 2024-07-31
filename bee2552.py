"""Beecrowd | 2552"""

def count_adjacents(matrix: list[list[int]], position: tuple[int]) -> int:
    top = (position[0] - 1, position[1]) if position[0] - 1 > -1 else None
    left = (position[0], position[1] - 1) if position[1] - 1 > -1 else None
    bottom = (position[0] + 1, position[1]) if position[0] + 1 < len(matrix) else None
    right = (position[0], position[1] + 1) if position[1] + 1 < len(matrix[0]) else None

    iteration = [i for i in (top, left, bottom, right) if i is not None]

    sum = 0
    for (i, j) in iteration:
        sum += matrix[i][j]

    return sum


while True:
    try:
        lines, columns = (int(x) for x in input().split())

        matrix = []
        for i in range(lines):
            matrix.append([int(x) for x in input().split()])

        result = [[0 for _ in range(columns)] for _ in range(lines)]
        for i in range(lines):
            for j in range(columns):
                result[i][j] = 9 if matrix[i][j] else count_adjacents(matrix, (i, j))

        for i in result:
            print(str(i)
                  .replace('[', '')
                  .replace(']', '')
                  .replace(', ', ''))
    except EOFError:
        break
