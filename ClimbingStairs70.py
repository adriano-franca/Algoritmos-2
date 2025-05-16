def climbStairs(n, memo=dict()):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n in memo: 
        return memo[n]
    else:
        memo[n] = climbStairs(n-1, memo)+climbStairs(n-2, memo)
        return memo[n]
    
#Caso de teste
n = 2
climbStairs(n, memo=dict())