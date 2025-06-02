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


# Caso de teste
trips = [[2,1,5],[3,3,7]]
capacity = 5
print(carPooling(trips, capacity))