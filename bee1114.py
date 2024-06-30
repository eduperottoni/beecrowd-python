"""Beecrowd | 1114"""

PASSWORD = 2002
while True:
    attempt = int(input())
    if PASSWORD != attempt:
        print('Senha Invalida')
        continue
    print('Acesso Permitido')
    break
