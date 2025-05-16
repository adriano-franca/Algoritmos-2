def isPalindrome(x):
    lista = [str(digito) for digito in str(x)]
    i = 0
    j = len(lista)-1
    print(lista)
    while(i<j):
        if lista[i] != lista[j]:
            return False
        i+=1
        j-=1
    return True

#Caso de teste
x = 1221122
print(isPalindrome(x))
