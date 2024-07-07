"""Beecrowd | 1827"""

while True:
    try:
        n = int(input())
        ones_limit = int(n/3) - 1
        matrix = []
        for i in range(n):
            line = []
            for j in range(n):
                # central cell
                if i == j == int(n/2):
                    line.append(4)
                # ones
                elif (
                    n - ones_limit - 1 > i > ones_limit
                    and n - ones_limit - 1 > j > ones_limit
                ):
                    line.append(1)
                # main diagonal
                elif i == j:
                    line.append(2)
                # secondary diagonal
                elif i == n - j - 1:
                    line.append(3)
                else:
                    line.append(0)
            matrix.append(line)

        # Printing
        for row in matrix:
            print(''.join(str(i) for i in row))
        print()
    except EOFError:
        break
