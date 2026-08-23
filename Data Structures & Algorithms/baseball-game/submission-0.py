#Implement an integer stack, following LIFO principles. Last In, First Out

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = [] #Ints only
        #1,2,+,C,5,D = 18
        # (stack) [], [1], [1,2], [1,2,3], [1,2], [1,2,5], [1,2,5,10]
        # (stack_ind) 0, 1, 2, 3, 2, 3, 4
        
        stack_ind = 0
        
        for operation in operations: # O (n)

            if operation == "+":
                stack.append(stack[stack_ind-2] + stack[stack_ind-1])
                stack_ind += 1
            elif operation == "C":
                stack.pop() #Removes the last element, LIFO principles fulfilled
                stack_ind -= 1
            elif operation == "D":
                stack.append(stack[stack_ind-1]*2)
                stack_ind += 1
            else:
                stack.append(int(operation))
                stack_ind += 1

        return sum(stack)