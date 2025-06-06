import heapq

def carPooling(trips, capacity):
    #trips - passageiros, inicio, fim
    maxHeap = []
    for num, start, end in trips:
        maxHeap.append((start, num))
        maxHeap.append((end, -num))
    heapq.heapify(maxHeap)
    while maxHeap:
        capacity -= heapq.heappop(maxHeap)[1]
        if capacity < 0:
            return False
    return True
def carPooling2(trips, capacity):
    maxHeap = []

    for i in range(len(trips)):
        #passageiros subindo
        heapq.heappush(maxHeap, (trips[i][1], trips[i][0]))
        #passageiros descendo
        heapq.heappush(maxHeap, (trips[i][2], -trips[i][0]))

    heapq.heapify(maxHeap)

    while len(maxHeap) != 0:
        capacity -= heapq.heappop(maxHeap)[1]
        if capacity < 0:
            return False
    return True

# Caso de teste
trips = [[2,1,5],[3,3,7]]
capacity = 5
print(carPooling2(trips, capacity))