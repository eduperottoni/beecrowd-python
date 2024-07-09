"""Beecrowd | 1318"""

while True:
    originals, present = (int(x) for x in input().split(' '))

    if originals == present == 0:
        break

    original_tickets = []
    repeated_tickets = []
    repeated_counter = 0
    for ticket in input().split(' '):
        if ticket not in original_tickets:
            original_tickets.append(ticket)
        else:
            if ticket not in repeated_tickets:
                repeated_tickets.append(ticket)
                repeated_counter += 1
    print(repeated_counter)
