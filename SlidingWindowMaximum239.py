import heapq

#Time Limit Exceeded

def maxSlidingWindow(nums, k):    
    maxHeap = [ (-nums[i], i) for i in range(k)]
    heapq.heapify(maxHeap)
    output = []
    startWindow = 0
    endWindow = k-1
    nextNum = -999999
    while True:
        maxVal, index = maxHeap[0]
        if -maxVal >= nextNum and index >= startWindow:
            output.append( -maxVal )
        elif -maxVal < nextNum:
            maxHeap = [(-nextNum, endWindow)]
            output.append( nextNum )
        else:
            j = startWindow
            maxHeap = [(-nums[j], j) for j in range(j, j+k, 1)]
            heapq.heapify(maxHeap)
            maxVal, index = maxHeap[0]
            output.append( -maxVal )
        endWindow +=1
        if endWindow >= len (nums):
            break
        nextNum = nums[endWindow]
        startWindow +=1
    return output

#Caso de teste
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))