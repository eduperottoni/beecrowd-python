"""Beecrowd | 1435"""
import math

while True:
    n = int(input())
    if n == 0:
        break
    quarter_n = math.ceil(n/2)

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < quarter_n:
                # 1st quarter
                if j < quarter_n:
                    matrix[i][j] = min(i, j) + 1
                # 2nd quarter
                else:
                    matrix[i][j] = matrix[i][n - j - 1]
            else:
                # 3rd & 4th quarter
                matrix[i][j] = matrix[n - i - 1][j]

    # Print formatting
    for row in matrix:
        line_str = []
        for col in row:
            line_str.append(str(col).rjust(3))
        print(' '.join(line_str))
    print()
