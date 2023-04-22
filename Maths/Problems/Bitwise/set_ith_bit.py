"""
Set the i'th bit
  if it's 0 make it 1
  if it's 1 make it 0
"""


def toggle_bit(num, i):  # Convert 0 to 1
    mask = 1 << i
    return num | mask


print(toggle_bit(86, 3))  # 94


def toggle_bit1(num, i):  # Covert 1 to 0
    mask = 1 << i
    return num ^ mask


print(toggle_bit1(86, 4))  # 70
print(toggle_bit1(86, 1))  # 84
print(toggle_bit1(86, 2))  # 82
