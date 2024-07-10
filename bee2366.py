"""Beecrowd | 2366"""

water_spots, athlete_distance = (int(x) for x in input().split())
ws_positions = [int(x) for x in input().split()]

if ws_positions[-1] != 42195:
    ws_positions.append(42195)

finishes = True
for i, position in enumerate(ws_positions):
    if i > 0:
        if position - ws_positions[i - 1] > athlete_distance:
            finishes = False
            break

print('S' if finishes else 'N')
