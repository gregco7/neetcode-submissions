class Solution:
    def countBits(self, n: int) -> List[int]:

        ourResult = [0] * (n+1)
        offset = 1

        for i in range(1, n+1): # [1,n]
            
            if i == (offset * 2):
                offset = i
                ourResult[i] = 1
            else:
                ourResult[i] = 1 + ourResult[i - offset]
        
        return ourResult

