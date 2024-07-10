"""Beecrowd | 1430"""

notes_duration = {'W': 1,
                  'H': 1/2,
                  'Q': 1/4,
                  'E': 1/8,
                  'S': 1/16,
                  'T': 1/32,
                  'X': 1/64}

while True:

    composition = [x for x in input().split('/') if x]

    if composition == ['*']:
        break

    right_measures = 0
    for i in composition:
        measure_time = 0
        for x in i:
            measure_time += notes_duration[x]
        if measure_time == 1:
            right_measures += 1
    print(right_measures)
