import heapq

def deleteGreatestValue(grid):
    heaps = []
    m = len(grid)
    n = len (grid[0])

    for row in grid:
        maxHeap = [-num for num in row]
        heapq.heapify(maxHeap)
        heaps.append(maxHeap)

    soma = 0

    for _ in range(n):
        removido = []

        for heap in heaps:
            maxValRow = -heapq.heappop(heap)
            removido.append(maxValRow)

        soma += max(removido)
    
    return soma

#Caso de teste
grid = [[1,2,4],[3,3,1]]
print(deleteGreatestValue(grid))
