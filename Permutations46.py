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