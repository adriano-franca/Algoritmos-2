def climbStairs(n, memo=dict()):
    if n<=3:
        return n
    elif n in memo: 
        return memo[n]
    else:
        memo[n] = climbStairs(n-1, memo)+climbStairs(n-2, memo)
        return memo[n]
    
#Caso de teste
n = 4
print(climbStairs(n, memo=dict()))

def climbStairsIter(n):
    if n<=3: return n
    #return climbStairsIter(n-1, memo)+climbStairsIter(n-2, memo)
    memo = [0, 1, 2, 3]
    def pd(n):
        while n+1>len(memo):
            memo.append(memo[-1] + memo[-2])
        return memo[n]
    return pd(n)

print(climbStairsIter(n))