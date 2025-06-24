def maxProFit(prices):
    menorValorAnterior = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        #profit = prices[i] - menorValorAnterior
        menorValorAnterior = min(menorValorAnterior, prices[i])
        profit = max(prices[i] - menorValorAnterior, profit)
    return profit
    
# Caso de teste
prices = [7,1,5,3,6,4]
print (maxProFit(prices))
prices = [7,6,4,3,1]
print (maxProFit(prices))