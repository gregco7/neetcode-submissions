class Solution:
    def reverseBits(self, n: int) -> int:

        # Given a 32-bit unsigned integer n, reverse the bits of the binary representation
        # of n and return the result

        # 32 0's to be fulfilled

        big = 2147483648 # a 32-bit integer of 1 + 31 0's
        res = 0

        while n:
            if n % 2:
                res += big

            n = n >> 1
            big = big // 2
        
        return res

        