def sortColors(nums):
    i = 0
    j = len(nums)-1
    while i <= j:
        if nums[i] == 0:
            i+=1
        elif nums[j] == 0:
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux
            i+=1
            j-=1
        else:
            j-=1
    j = len(nums)-1
    while i <= j:
        if nums[i] == 1:
            i+=1
        elif nums[j] == 1:
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux
            i+=1
            j-=1
        else:
            j-=1

#Caso de teste
nums = [2,0,2,1,1,0]
print(sortColors(nums))