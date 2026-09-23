class Solution:

    def isalnum(self,c):
        return ( (ord("a") <= ord(c) <= ord("z")) or (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <= ord(c) <= ord("9")))

    def isPalindrome(self, s: str) -> bool:

        leftPointer = 0
        rightPointer = len(s) - 1

        while rightPointer > leftPointer:
            
            while (leftPointer < rightPointer) and (not self.isalnum(s[leftPointer])):
                leftPointer += 1
            while (rightPointer > leftPointer) and (not self.isalnum(s[rightPointer])):
                rightPointer -= 1
            
            if (s[leftPointer].lower() == s[rightPointer].lower()):
                leftPointer += 1
                rightPointer -= 1
            else:
                print(leftPointer,rightPointer)
                return False

        return True

        

        

            

        