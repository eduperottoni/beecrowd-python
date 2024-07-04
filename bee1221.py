"""Beecrowd | 1221"""


def check_if_prime(n: int) -> bool:
    """Just checks if a number is prime iterating up to the sqrt(n)
    see https://programmercave.com/blog/2023/02/28/Optimized-Algorithm-for-Checking-Prime-Numbers-A-Comprehensive-Guide#:~:text=The%20most%20basic%20algorithm%20to,number%20is%20a%20prime%20number.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if i * i <= n:
            if n % i == 0:
                return False
        else:
            break
    return True


cases = int(input())
for i in range(cases):
    print('Prime' if check_if_prime(int(input())) else 'Not Prime')
