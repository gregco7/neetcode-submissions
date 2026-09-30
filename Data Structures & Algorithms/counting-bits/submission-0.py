class Solution:
    def countBits(self, n: int) -> List[int]:

        def countOnes(n):
            count = 0
            
            while n:
                count += (n%2)
                n = n >> 1 # shift binary to the right by one with ` x >> 1 `
                
            return count

        arr = []
        for i in range(n+1):
            val = countOnes(i)
            arr.append(val)

        return arr

        