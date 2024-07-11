"""Beecrowd | 1911"""

while True:

    sig_list_qtd = int(input())
    if sig_list_qtd == 0:
        break

    sig_list = {}
    for i in range(sig_list_qtd):
        key, name = [x for x in input().split()]
        sig_list[key] = name
    stud_qtd = int(input())
    wrong_names = 0
    for i in range(stud_qtd):
        wrong_letters = 0
        stud_key, stud_sign = [x for x in input().split()]
        for i in range(len(sig_list[stud_key])):
            if (sig_list[stud_key])[i] != stud_sign[i]:
                wrong_letters += 1
        if wrong_letters > 1:
            wrong_names += 1
    print(wrong_names)
