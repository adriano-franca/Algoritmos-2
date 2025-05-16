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


def combine(n, k):
    output = []

    def bt(partial=[]):
        if len(partial)==k:
            output.append(partial.copy())
        else:
            first_elem = 1 if len(partial)==0 else partial[-1]+1
            for elm in range(first_elem, n+1):
                
                print(len(partial)+n<k)
                bt(partial+[elm])
        
    bt([])
    return output

nums = [1,2,3]
n = 4
k = 2

t = combine(n, k)
print(t)