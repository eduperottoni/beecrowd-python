"""Beecrowd | 1023"""

import math

city_id = 1

while True:
    houses = int(input(''))

    if not houses:
        break

    if city_id > 1:
        print("")

    city_info: list[dict[int, int]] = []
    total_consum, total_residents = 0, 0
    for i in range(houses):
        residents, house_consum = (int(x) for x in input('').split(' '))
        total_consum += house_consum
        total_residents += residents
        city_info.append((residents, int(house_consum/residents)))
    city_info.sort(key=lambda x: x[1])

    # Output
    print(f"Cidade# {city_id}:")
    print(" ".join(str(x).replace(", ", "-").replace("(", "").replace(")", "") for x in city_info))
    print(f'Consumo medio: {(math.floor(total_consum/total_residents * 10 ** 2) / 10 ** 2):.2f} m3.')
    city_id += 1
