import heapq

def nthUglyNumber(n):
    contador = 0
    prev = 0
    minHeap = [1]
    
    while contador < n:
        atual = heapq.heappop(minHeap)
        if atual == prev:
            continue
        heapq.heappush(minHeap, atual * 2)
        heapq.heappush(minHeap, atual * 3)
        heapq.heappush(minHeap, atual * 5)
        prev = atual
        contador +=1

    return prev

n = 10
nthUglyNumber(n)