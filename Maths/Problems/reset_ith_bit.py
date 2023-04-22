"""
Reset 4th bit
    1 0 1 0 1 1 0
  & 1 1 0 1 1 1 1
  -----------------
    1 0 0 0 1 1 0
Q: How to get the mask?
A: Complement the mask.

"""


def reset_ith_bit(num, i):  # only for '1 -> 0'
    mask = ~(1 << i)
    return num & mask


print(reset_ith_bit(86, 4))  # 70
print(reset_ith_bit(86, 2))  # 82
print(reset_ith_bit(86, 1))  # 84


# print(reset_ith_bit(86, 3)) # wrong

def reset_ith_bit1(num, i):
    mask = 1 << i
    return num | mask


print(reset_ith_bit1(86, 3))  # 94
