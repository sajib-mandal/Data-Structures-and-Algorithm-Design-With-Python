def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(13))  # True
print(is_prime(12))  # False
print(is_prime(17))  # False