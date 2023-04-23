def is_prime(n):
    if n <= 1:
        return False

    c = 2
    while c * c <= n:
        if n % c == 0:
            return False
        c += 1
    return True


count = 0
n = 40
for i in range(2, n + 1):
    if is_prime(i):
        count += 1
print(count)  # 12
