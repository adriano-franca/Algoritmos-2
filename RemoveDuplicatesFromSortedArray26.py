def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]    
    return i+1

#Caso de teste
nums = [1,1,2]
print(removeDuplicates(nums))