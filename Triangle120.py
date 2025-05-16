def minPath(triangle, lin, col, memo):
    if lin==len(triangle)-1:
        return triangle[lin][col]
    elif (lin, col) in memo:
        return memo[(lin, col)]
    else:
        child1 = minPath(triangle, lin+1, col, memo)
        child2 = minPath(triangle, lin+1, col+1, memo)
        memo[(lin, col)] = min(child1, child2)+triangle[lin][col]
        return memo[(lin, col)]

def minimumTotal(triangle):
    memo = dict()
    return minPath(triangle, 0, 0, memo)

#Caso de teste
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))