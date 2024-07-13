"""Beecrowd | 2471"""

n = int(input())

matrix = []

line_index = col_index = diff_value = -1
sums = {}

for i in range(n):
    matrix.append([int(x) for x in input().split()])
    if sum(matrix[i]) in sums:
        sums[sum(matrix[i])][0] += 1
        sums[sum(matrix[i])][1] = i
    else:
        sums[sum(matrix[i])] = [1, i]

for value in sums.values():
    if value[0] == 1:
        line_index = value[1]

for i in range(n):
    col_sum = sum(line[i] for line in matrix)

    value = sums[col_sum]
    if value[0] == 1:
        col_index = i
        diff_value = col_sum

list = list(sums.keys())
list.remove(diff_value)
current_number = matrix[line_index][col_index]
print(f'{current_number + (list[0] - diff_value)} {current_number}')
