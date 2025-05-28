def hammingWeight(n):
    numeroEmBinario = bin(n)[2:]
    contador = 0
    for i in range(len(numeroEmBinario)):
        if numeroEmBinario[i] == '1':
            contador+=1
    return contador

#Caso de teste
n = 2147483645
print(hammingWeight(n))
