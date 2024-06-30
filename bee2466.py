"""Beecrowd | 2466"""

balls = int(input(''))
queue = [int(x) for x in input('').split(' ')]

while len(queue) > 1:
    new_queue = [0 for x in range(len(queue) - 1)]
    for i, item in enumerate(new_queue):
        if queue[i] == queue[i + 1]:
            new_queue[i] = 1
        else:
            new_queue[i] = -1

    queue = new_queue

if queue[0] == -1:
    print('branca')
else:
    print('preta')
