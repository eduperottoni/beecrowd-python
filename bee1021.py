"""Beecrowd | 1021"""

value = float(input())

notes = {
  100: 0,
  50: 0,
  20: 0,
  10: 0,
  5: 0,
  2: 0
}

coins = {
  1: 0,
  0.5: 0,
  0.25: 0,
  0.10: 0,
  0.05: 0,
  0.01: 0
}

print('NOTAS:')
for note in notes:
    notes[note] = int(value / note)
    value -= notes[note] * note
    print(f'{notes[note]:.0f} nota(s) de R$ {note}.00')

print('MOEDAS:')
for coin in coins:
    value = round(value, 2)
    coins[coin] = int(value / coin)
    value -= coins[coin] * coin
    print(f'{coins[coin]:.0f} moeda(s) de R$ {coin:.2f}')
