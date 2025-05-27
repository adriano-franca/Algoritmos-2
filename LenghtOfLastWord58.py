def lengthOfLastWord(s):
    s = s.split()
    ultima = s[len(s) - 1]
    return len(ultima)

#Caso de teste
s = "Hello World"
print(lengthOfLastWord(s))