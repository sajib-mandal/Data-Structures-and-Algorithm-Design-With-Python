import math


def rightmost_set_bit(n):
    # If n is 0, there are no set bits
    if n == 0:
        return -1

    # Use the bitwise AND operator to isolate the rightmost set bit
    rightmost_bit = n & -n

    # Use logarithmic function to calculate the position of the rightmost bit
    # Adding 1 because log function returns in float and we need to return position in integer
    position = int(math.log2(rightmost_bit)) + 1

    return position


print(rightmost_set_bit(182))  # 2
