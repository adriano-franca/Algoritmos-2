def findMedianSortedArrays(self, nums1, nums2):
    i=0
    nums3 = []
    for i in range(len(nums1)):
        nums3.append(nums1[i])
        i+=1
    i=0
    for i in range(len(nums2)):
        nums3.append(nums2[i])
        i+=1
    nums3.sort()
    if len(nums3) %2 == 0:
        meio = len(nums3)//2
        mediana = float((nums3[meio]+nums3[meio-1]))/2
        return mediana
    meio = len(nums3)//2
    return nums3[meio]

#Caso de teste
nums1 = [1,2], nums2 = [3,4]
findMedianSortedArrays(nums1, nums2)