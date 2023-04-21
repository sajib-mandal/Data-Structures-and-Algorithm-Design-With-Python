def get_ith_bit(num, i):
    # bitmask = 1 << i
    # return (num & bitmask) >> i
    return (num >> i) & 1  # both are working


print(get_ith_bit(182, 5))  # 1
