"""Beecrowd | 2482"""


languages = int(input())
translations = {}
for i in range(languages):
    lang = input()
    traduction = input()
    translations[lang] = traduction

children = int(input())
for i in range(children):
    name = input()
    lang = input()
    print(name)
    print(translations[lang])
    print()
