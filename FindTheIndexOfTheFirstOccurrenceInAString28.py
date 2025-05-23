def strStr(haystack, needle):
    cont = 0
    j = 0
    k = 0
    for i in range(len(haystack)-1):
        if haystack[i] == needle[j]:
            index = i
            k = i
            while haystack[k] == needle[j] and j<=len(needle)-1:
                cont +=1
                j+=1
                k+=1
        else:
            cont = 0
            j = 0
    if len(needle) == cont:
        return index
    return -1

#Caso de teste
f = "sadbutsad"
g = "sad"
print(strStr(f, g))
        