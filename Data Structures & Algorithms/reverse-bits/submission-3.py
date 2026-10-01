class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        big = 1 << 31

        while n:

            if n & 1:
                res |= big
            
            big >>= 1
            n >>= 1
        
        return res

        