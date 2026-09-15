class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeroStudents = 0
        oneStudents = 0

        for student in students:
            if student == 0:
                zeroStudents += 1
            else:
                oneStudents += 1
        
        for sandwich in sandwiches:
            if sandwich == 0:
                if zeroStudents > 0:
                    zeroStudents -= 1
                else:
                    return oneStudents
            
            if sandwich == 1:
                if oneStudents > 0:
                    oneStudents -=1
                else:
                    return zeroStudents
        
        return 0