"""Beecrowd | 1514"""


def count_score(matrice):
    """Conta pontuação"""
    compet = len(matrice)
    problems = len(matrice[0])
    score_matrice = [1, 1, 1, 1]
    # Alguém resolveu todos
    for comp in matrice:
        if 0 not in comp:
            score_matrice[0] = 0
            break
    # Alguém resolveu zero problemas
    for comp in matrice:
        if sum(comp) == 0:
            score_matrice[3] = 0
            break
    # Algum problema não foi resolvido
    # Algum problema foi resolvido por todos
    problems_matrice = [0 for x in range(problems)]
    for i in range(problems):
        for comp in matrice:
            problems_matrice[i] += comp[i]
    if compet in problems_matrice:
        score_matrice[2] = 0
    if 0 in problems_matrice:
        score_matrice[1] = 0
    return sum(score_matrice)


while True:
    competitors, problems = [int(x) for x in input().split()]
    if competitors == problems == 0:
        break
    matrice = []
    for i in range(competitors):
        matrice.append([int(x) for x in input().split()])
    print(count_score(matrice))
