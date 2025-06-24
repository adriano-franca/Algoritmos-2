def fatorial(n, memo=dict()):
    if n in memo:
        return memo[n]
    if n==0:
        memo[n] = 1
        return 1
    else:
        memo[n] = n * fatorial(n-1, memo)
        return memo[n]