def fib_iter(n):
    memo = [0,1]
    for i in range(2, n+1):
        memo.append(memo[-1] + memo[-2])
    return memo[n]

def fib_iter2(n, memo):
    while n+1 > len(memo):
        memo.append(memo[-1] + memo[-2])
    return memo[n]

# Caso de teste
n = 10
print(fib_iter(n))