"""Beecrowd | 2229"""

n_teste = 1
while True:
    n = int(input())
    if n == -1:
        break
    print(f'Teste {n_teste}')
    print((2 ** n + 1) ** 2)
    print()
    n_teste += 1
