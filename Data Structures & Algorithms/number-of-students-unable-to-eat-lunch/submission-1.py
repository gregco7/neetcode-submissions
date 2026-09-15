class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        for index,sandwich in enumerate(sandwiches):
            if sandwich in students:
                ourStudent = students.index(sandwich)
                students.pop(ourStudent)
            else:
                return len(sandwiches) - index

        return 0