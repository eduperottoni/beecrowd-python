"""Beecrowd | 2313"""

side1, side2, side3 = [int(x) for x in input().split()]

if (
    side1 <= side2 + side3
    and side2 <= side1 + side3
    and side3 <= side2 + side1
):

    if side1 == side2 == side3:
        print('Valido-Equilatero')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')

    if (
        side1**2 == side2**2 + side3**2
        or side2**2 == side1**2 + side3**2
        or side3**2 == side2**2 + side1**2
    ):
        print('Retangulo: S')
    else:
        print('Retangulo: N')

else:
    print('Invalido')
