"""Beecrowd | 1023"""

import math

while True:
    city_id = 1
    houses = int(input(''))
    city_info: list[dict[int, int]] = []
    total_consum, total_residents = 0, 0
    for i in range(houses):
        residents, house_consum = (int(x) for x in input('').split(' '))
        total_consum += house_consum
        total_residents += residents
        city_info.append((residents, int(house_consum/residents)))
    city_info.sort(key=lambda x: x[1])
    print(city_info)
    print(f'Consumo medio: {math.floor(total_consum/total_residents * 10 ** 2) / 10 ** 2} m3.')

