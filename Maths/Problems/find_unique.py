def find_unique(nums):
    unique = 0

    # Work only negative number
    # for num in nums:
    #     unique ^= num
    # return unique

    # Work for both negative and positive
    for num in nums:
        if num < 0:
            num = abs(num)
        unique ^= num
    return unique


print(find_unique([2, 3, 3, 4, 2, 6, 4])) # 6
print(find_unique([-2, 3, 2, 4, -5, 5, -4])) # 3

