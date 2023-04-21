"""
Questions:
  Give a number find if it is odd or even
"""


def is_odd(n):
    return (n & 1) == 1


print(is_odd(66)) # False
print(is_odd(67)) # True
