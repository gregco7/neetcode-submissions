class Solution:
    def isPalindrome(self, s: str) -> bool:

        modStr = ""
        for char in s:
            if char.isalnum(): modStr += char.lower();

        return modStr == modStr[::-1]

            

        