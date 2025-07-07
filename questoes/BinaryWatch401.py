def time_to_string(hour, minute):
        return str(hour)+":"+("0"+str(minute))[-2:]

def leds(hour, minute):
        return bin(hour).count("1") + bin(minute).count("1")

def readBinaryWatch(turnedOn):
    out = []
    for i in range(12):
        for j in range(60):
            numLeds = leds(i, j)
            if numLeds == turnedOn:
                result = time_to_string(i, j)
                out.append(result)
    return out

#Caso de teste
turnedOn = 4
print(readBinaryWatch(turnedOn))