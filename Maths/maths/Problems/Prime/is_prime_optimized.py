"""
1 * 36
2 * 18
3 * 12
4 * 9
6 * 6
[AVOID half of the number because ('1 * 2' and '2 * 1') are same]
9 * 4
12 * 3
18 * 2
36 * 1
"""


def is_prime(n):
    if n <= 1:
        return False

    c = 2
    while c * c <= n:
        if n % c == 0:
            return False
        c += 1
    return True


print(is_prime(37))

# n = 20
# for i in range(1, n+1):
#     print(f"{i} {is_prime(i)}")
