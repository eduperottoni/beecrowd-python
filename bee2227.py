"""Beecrowd | 2227"""

counter = 1
while True:
    airports, flights = (int(x) for x in input().split())

    if airports == flights == 0:
        break

    airports_info = [0 for _ in range(airports)]
    for f in range(flights):
        source, target = (int(x) for x in input().split())
        airports_info[source - 1] += 1
        airports_info[target - 1] += 1

    maximun = max(airports_info)
    answer = []
    for i, a in enumerate(airports_info):
        if a == maximun:
            answer.append(str(i + 1))

    print(f'Teste {counter}')
    print(' '.join(answer), '')
    print()

    counter += 1
