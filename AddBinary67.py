def addBinary(a, b):
    #Transforma as duas strings binárias em interos
    a = int(a, 2)
    b = int(b, 2)
    
    #Retorna a soma dos dois inteiros como uma string binária, exluindo o prefixo
    return bin(a+b)[2:]

#Caso de teste
print(addBinary("10", "110"))