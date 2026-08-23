#Solve valid parantheses problem by adding left brackets to a stack, and verifying their removal fulfills LIFO principles.

class Solution:

    #Return 0 for left Bracket, 1 for right bracket. Returns None if invalid character
    def matchingBracket(self, char_left:str,char_right:str) -> Optional[int]:
        intendedRight = ""

        match char_left:
            case "(":
                intendedRight = ")"
            case "[":
                intendedRight = "]"
            case "{":
                intendedRight = "}"
        
        return char_right == intendedRight

    def isValid(self, s: str) -> bool:
        stack = [] #[], [
        

        for char in s:

            if char in ")]}":
                #We are touching the next right char, and the this bracket char should equal the popped char from stack.
                #If no left brackets in stack to fulfill right bracket, return false.

                if len(stack) == 0:
                    return False

                popped_Character = stack.pop(-1)
                if not self.matchingBracket(popped_Character,char):
                    return False
                
            else:
                stack.append(char)
                

        return len(stack) == 0
        # [], inv = 0, stack = []. True?
        # {[(]}, inv = 3, stack = [ {,[,( ]. False?

        