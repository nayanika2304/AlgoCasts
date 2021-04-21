def square_numbers(nums):
    neg_i = -1
    i = 0

    result = []
    for n in nums:
        if n >= 0:
            if neg_i == -1:
                neg_i = i - 1

            while neg_i >= 0 and nums[neg_i] < 0 and -nums[neg_i] < nums[i]:
                val = nums[neg_i]
                result.append(val * val)
                neg_i -= 1

            val = nums[i]
            result.append(val * val)
        i += 1

    while neg_i >= 0 and nums[neg_i] < 0:
        val = nums[neg_i]
        result.append(val * val)
        neg_i -= 1

    return result


print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
