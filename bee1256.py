"""Beecrowd | 1256"""

hash_tables = []

cases = int(input())
for case in range(cases):
    hash_table = {}
    # Dict can be considered a hash table
    entries_num, keys_num = [int(x) for x in input().split(' ')]
    # Creates the hash entries
    for i in range(entries_num):
        hash_table[i] = []
    keys = [int(x) for x in input().split(' ')]
    # Populates the hash table
    for key in keys:
        hash_table[key % entries_num].append(key)

    hash_tables.append(hash_table)


for i, hash_table in enumerate(hash_tables):
    print(str(hash_table)
          .replace(": [", " -> ")
          .replace("], ", " -> \\\n")
          .replace("]", " -> \\")
          .replace("{", "")
          .replace("}", "")
          .replace(",", " ->")
          .replace("->  ->", "->"))
    if i < len(hash_tables) - 1:
        print()
