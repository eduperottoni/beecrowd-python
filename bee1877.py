"""Beecrowd | 1877"""

towers, peaks = (int(x) for x in input().split(' '))
heights = [int(x) for x in input().split(' ')]

peaks_counter = 0
valleys_counter = 0
for index, h in enumerate(heights):
    if index != 0 and index != len(heights) - 1:
        if heights[index - 1] > h < heights[index + 1]:
            valleys_counter += 1
        elif heights[index - 1] < h > heights[index + 1]:
            peaks_counter += 1

print('beautiful' if (peaks_counter == peaks and valleys_counter == peaks - 1) else 'ugly')
