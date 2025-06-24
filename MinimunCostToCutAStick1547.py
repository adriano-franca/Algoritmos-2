def minCost(n, cuts):
    cuts.append(0)
    cuts.append(n)
    cuts.sort()

    memo = dict()

    def pd(left, right):
        if left==right-1:
            return 0

        if(left, right) in memo:
            return memo[(left, right)]

        cost = cuts[right] - cuts[left]
        
        min_cost = float("inf")
        for i in range(left+1, right):
            aux = pd(left, i) + pd(i, right) + cost
            min_cost = min(min_cost, aux)
        memo[(left, right)] = min_cost
        return min_cost

    return pd(0, len(cuts)-1)

#Caso de teste
n = 7
cuts = [1, 3, 4, 5]
print(minCost(n, cuts))