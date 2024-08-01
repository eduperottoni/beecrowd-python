"""Beecrowd | 2654"""

candidates = int(input())

candidates_list = []

for c in range(candidates):
    i = input().split()
    name = i.pop(0)
    power, kills, deaths = (int(x) for x in i)
    power, kills = 100 - power, 100 - kills
    data = (name, power, kills, deaths)
    candidates_list.append(data)

sorted_candidates = sorted(candidates_list, key=lambda data: (data[1], data[2], data[3], data[0]))

print(sorted_candidates[0][0])
