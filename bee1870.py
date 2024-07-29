"""Beecrowd | 1870"""


def search_fan(direction: str, index: int, line: int) -> int:
    fan_index = index
    if direction == 'left':
        for elem in reversed(line[:index + 1]):
            if elem != 0:
                return fan_index
            fan_index -= 1
    else:
        for elem in line[index:]:
            if elem != 0:
                return fan_index
            fan_index += 1


while True:
    lines, columns, start_position = (int(x) for x in input().split())
    if lines == columns == start_position == 0:
        break

    start_position -= 1
    final_status = ""

    for line in range(lines):
        l = [int(x) for x in input().split()]
        left = search_fan('left', start_position, l)
        right = search_fan('r', start_position, l)

        if left == start_position or right == start_position:
            final_status = f'BOOM {line + 1} {start_position + 1}'

        start_position += (l[left] - l[right])
        if l[start_position] != 0:
            final_status = f'BOOM {line + 1} {start_position + 1}'

    out = f'OUT {start_position + 1}'
    print(f'{final_status if final_status else out}')
