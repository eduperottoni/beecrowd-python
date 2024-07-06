"""Beecrowd | 1471"""

while True:
    try:
        mergulho, retorno = [int(x) for x in input().split()]
        vetor_mergulho = range(1, mergulho+1)
        vetor_retorno = [int(x) for x in input().split()]
        vetor_diferenca = [x for x in vetor_mergulho if x not in vetor_retorno]
        if mergulho == retorno:
            print('*')
        else:
            for i in vetor_diferenca:
                print(f'{i}', end=' ')
            print()
    except EOFError:
        break
