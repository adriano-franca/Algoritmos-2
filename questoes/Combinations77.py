def combine(n, k):
    output = []

    def bt(partial=[]):
        if len(partial)==k:
            output.append(partial.copy())
        else:
            first_elem = 1 if len(partial)==0 else partial[-1]+1
            for elm in range(first_elem, n+1):
                bt(partial+[elm])
        
    bt([])
    return output

#Caso de teste
n = 4
k = 2

t = combine(n, k)
print(t)