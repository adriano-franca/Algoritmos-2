def LISWithStartingIndex(nums, index, memo=dict()):
    maxSize = 1
    if index in memo:
        return memo[index]
    for i in range(index + 1, len(nums)):
        if nums[i] > nums[index]:
            size = 1 + LISWithStartingIndex(nums, i, memo)
            maxSize = max(maxSize, size)
    memo[index] = maxSize
    return maxSize

def lengthOfLIS(nums):
    maxSize = 0
    memo = {}
    for i in range(len(nums)):
        size = LISWithStartingIndex(nums, i, memo)
        maxSize = max(maxSize, size)
    return maxSize

'''def lengthOfLISBottomUp(nums):
    memo = [-1] * len(nums)
    memo[len(nums) - 1] = 1
    for i in range(len(nums) - 2, -1, -1):
        maxSequence = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                maxSequence = max(maxSequence, 1 + memo[j])
        memo[i] = 1+maxSequence
    return max(memo)
'''

# Caso de teste
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))