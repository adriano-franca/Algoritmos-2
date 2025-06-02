import heapq

def lastStoneWeight(stones):
    maxHeap = [-stone for stone in stones]
    heapq.heapify(maxHeap)
    print(maxHeap)
    while len(maxHeap) > 1:
        primeiroMaior = -heapq.heappop(maxHeap)
        segundoMaior = -heapq.heappop(maxHeap)
        novaPedra = primeiroMaior - segundoMaior
        if novaPedra > 0:
            heapq.heappush(maxHeap, -novaPedra)
    
    if len(maxHeap) == 0:
        return 0
    return -maxHeap[0]

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))
stones = [1,1]
print(lastStoneWeight(stones))
stones = [1, 3]
print(lastStoneWeight(stones))