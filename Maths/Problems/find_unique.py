def find_unique(nums):
    unique = 0

    for num in nums:
        unique ^= num
    return unique


print(find_unique([2, 3, 3, 4, 2, 6, 4]))

