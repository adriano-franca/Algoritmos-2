def permute(nums):
    output = []

    def bt(partial=[]):
        if(len(partial)==len(nums)):
            output.append(partial[:])
        else:
            for elm in nums:
                if elm not in partial:
                    bt(partial+[elm])

    bt([])
    return output

#Caso de teste
nums = [1,2,3]
print(permute(nums))