def permute(nums):
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            for k in range(len(nums)):
                if k == i or k == j:
                    continue
                result.append([nums[i], nums[j], nums[k]])

    return result
nums = [1, 2, 3]
permutations = permute(nums)
print("Original Collection:", nums)
print("Collection of Permutation:")
print(permutations)
