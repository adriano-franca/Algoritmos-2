def subsets(nums):
    output = []

    def bt(partial, index):
        if index>=len(nums):
            output.append(partial.copy())
        else:
            bt(partial, index+1)
            bt(partial+[nums[index]], index+1)

    bt([], 0)
    return output

#Caso de teste
nums = [1,2,3]
print(subsets(nums))