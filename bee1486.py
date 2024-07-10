"""Beecrowd | 1486"""

while True:
    proc_points, n_measures, min_lenght = (int(x) for x in input().split())

    if proc_points == n_measures == min_lenght == 0:
        break

    gte_than_min_lenght = 0
    measures: list[list[bool]] = []
    for m in range(n_measures):
        measure = [bool(int(x)) for x in input().split()]
        measures.append(measure)

    for p in range(proc_points):
        m_counter = 0

        proc_point_measures = [m[p] for m in measures]

        for i, v in enumerate(proc_point_measures):
            if v:
                m_counter += 1

            if not v or i == n_measures - 1:
                if m_counter >= min_lenght:
                    gte_than_min_lenght += 1
                m_counter = 0

    print(gte_than_min_lenght)
