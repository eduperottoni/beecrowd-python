"""Beecrowd | 1089"""


def check_if_peak(left, value, right) -> bool:
    """Checks whether a value is a peak"""
    return (left > value and right > value) or (left < value and right < value)


while True:
    samples_num = int(input())
    if samples_num == 0:
        break

    samples = [int(x) for x in input().split()]

    peak_counter = 0

    for i, sample in enumerate(samples):
        left = right = None
        if i == 0:
            left = samples[samples_num - 1]
            right = samples[i + 1]
        elif i == samples_num - 1:
            right = samples[0]
            left = samples[i - 1]
        else:
            right = samples[i + 1]
            left = samples[i - 1]

        if check_if_peak(left, sample, right):
            peak_counter += 1

    print(peak_counter)
