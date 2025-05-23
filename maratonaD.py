entrada = input().split()

e = int(entrada[0])
v = int(entrada[1])

horas = e//v
minutos = e%v
minutos = ((e*60)//v)%60
horarioFinal = (19 + horas) % 24

print("{}:{}".format(horarioFinal, minutos))
