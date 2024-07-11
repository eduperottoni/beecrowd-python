"""Beecrowd | 2091"""


while True:
    cases = int(input())
    try:
        for i in range(cases):
            num_dict = {}
            num_array = [int(x) for x in input().split()]
            for i in num_array:
                if i in num_dict:
                    num_dict[i] += 1
                else:
                    num_dict[i] = 1
            lon_numb = 0
            for k, v in num_dict.items():
                if v % 2 != 0:
                    lon_numb = k    
            if not len(num_array) == 1:
                print(lon_numb)

    except EOFError:
        break
