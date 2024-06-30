"""Beecrowd | 1449"""


instances = int(input(''))
for i in range(instances):
    translations = {}
    n_translations, music_lines = (int(x) for x in input('').split(' '))
    for n in range(n_translations):
        jpn_word = input('')
        pt_word = input('')
        translations[jpn_word] = pt_word
    for line in range(music_lines):
        line = input('')
        translated = " ".join((translations[x] if x in translations else x) for x in line.split(' '))
        print(translated)
    print('')
