class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # integer array digits
        # where each digits[i] 
        # is the ith digit of a large integer
        # ordered from most significant to least significant
        # it will not contain any leading zero

        # return the digits of the given integer after incrementing it by one

        ind = len(digits) - 1

        while (ind >= 0 and digits[ind] == 9):
            digits[ind] = 0
            ind -= 1
        
        if ind == -1:
            return [1] + digits
        else:
            digits[ind] += 1
            return digits
        

        
        
        


        