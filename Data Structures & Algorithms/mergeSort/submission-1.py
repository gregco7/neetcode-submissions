# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    #merge two sorted Lists
    def merge(self, LH:List[Pair],RH:List[Pair]):

        leftPointer = 0
        rightPointer = 0
        mergedList = []

        while ( (leftPointer < (len(LH)) ) and ( rightPointer<(len(RH)) )):
            if (RH[rightPointer].key < LH[leftPointer].key):
                mergedList.append(RH[rightPointer])
                rightPointer += 1
            else: 
                #Giving the left array the privelige of inheriting the equality case as well ensures stability in merge sort.
                mergedList.append(LH[leftPointer])
                leftPointer += 1
            
        mergedList += LH[leftPointer:]
        mergedList += RH[rightPointer:]
        return mergedList

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        pairsLength = len(pairs)
        # base case
        if (pairsLength <= 1): return pairs;

        middleIndex = pairsLength // 2
        leftHalf = self.mergeSort(pairs[:middleIndex])
        rightHalf = self.mergeSort(pairs[middleIndex:])

        return self.merge(leftHalf,rightHalf)


        



