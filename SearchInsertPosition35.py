def searchInsert(nums, target):
    esq, dir = 0, len(nums)-1

    while esq<=dir:
        meio = (esq+dir)//2

        if nums[meio] == target:
            return meio
        elif nums[meio] > target:
            dir = meio - 1
        else:
            esq = meio + 1
    return esq
    
nums = [1, 3, 5, 6, 7]
print(searchInsert(nums, 3))
#metade = len(nums)//2
#print(nums[:metade])