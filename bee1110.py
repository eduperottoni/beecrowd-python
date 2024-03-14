"""Beecrowd | 1110"""

import queue

while True:
    q = queue.SimpleQueue()
    discarded = []

    cards_num = int(input())
    if cards_num == 0:
        break
    for i in range(1, cards_num + 1):
        q.put(i)
    
    while (q.qsize() > 1):
        discarded.append(q.get())
        q.put(q.get())
   
    print(f"Discarded cards: {str(discarded)[1:-1]}")
    print(f"Remaining card: {q.get()}")