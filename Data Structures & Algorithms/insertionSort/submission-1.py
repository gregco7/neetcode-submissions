# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        if len(pairs) > 0:
            our_list = [pairs[:]]

            # 5,2,9 
            # 

            for i in range(1,len(pairs)):
                j = i-1
                
                while (j>=0 and pairs[j+1].key < pairs[j].key):
                    #switch, then append to our list 
                    temp = pairs[j+1] # 3,4 .. temp = 4, 4 = 3 ... 3, 3, 
                    pairs[j+1] = pairs[j]
                    pairs[j] = temp
                    j-=1

                our_list.append(pairs[:])
                
            return our_list
        else:
            return []


        

        