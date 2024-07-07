"""Beecrowd | 1383"""

cases = int(input())


def verify_lines(matrix: list[list[int]]) -> bool:
    """Verifica linhas com números únicos"""
    for row in matrix:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True


def verify_columns(matrix: list[list[int]]) -> bool:
    """Verifica colunas com números únicos"""
    for j in range(9):
        column = []
        for row in matrix:
            if row[j] in column:
                return False
            else:
                column.append(row[j])
    return True


def verify_squads(matrix: list[list[int]]) -> bool:
    """Verifica subquadrados"""
    squads = [[] for _ in range(9)]
    for index, row in enumerate(matrix):
        for i in range(3):
            squads[int(index/3) * 3 + i] += row[i*3:(i+1)*3]
    return verify_lines(squads)


for i in range(cases):

    matrix = []
    for row in range(9):
        line = [int(x) for x in input().split(' ')]

        matrix.append(line)

    print(f'Instancia {i + 1}')
    if (
        verify_lines(matrix)
        and verify_columns(matrix)
        and verify_squads(matrix)
    ):
        print('SIM\n')
    else:
        print('NAO\n')
