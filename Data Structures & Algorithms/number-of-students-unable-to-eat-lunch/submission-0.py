class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        def shiftStudents(num:int):
            for _ in range (num):
                frontStudent = students.pop(0)
                students.append(frontStudent)
            
        
        for index,sandwich in enumerate(sandwiches):

            if sandwich in students:
                count = 0 
                for student in students:
                    if sandwich != student:
                        count+=1
                    else:
                        break
                shiftStudents(count)
                students.pop(0)
                    
            else:
                return len(sandwiches) - index
        return 0
        
            

                


        