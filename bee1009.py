"""Beecrowd | 1009"""


name = input()
fixed_salary = float(input())
sale = float(input())
bonus_salary = sale*0.15
total_salary = fixed_salary + bonus_salary
print(f'TOTAL = R$ {total_salary:.2f}')
