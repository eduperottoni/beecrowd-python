"""Beecrowd | 2139"""

days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        month, day = (int(x) for x in input().split(' '))
        if day > 25 and month == 12:
            print('Ja passou!')
        elif day == 25 and month == 12:
            print('E natal!')
        elif day == 24 and month == 12:
            print('E vespera de natal!')
        else:
            passed_days = sum(days_per_month[:month - 1]) if month >= 2 else 0
            passed_days = passed_days + day
            print(f'Faltam {360 - passed_days} dias para o natal!')
    except EOFError:
        break
