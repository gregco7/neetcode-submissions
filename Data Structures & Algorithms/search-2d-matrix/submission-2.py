class Solution:

    def intoVal(self,ind,rows,cols,m):
        rowInd = (ind // cols) 
        colInd = (ind % cols)
        if rowInd < len(m) and  colInd < len(m[rowInd]):
            return m[rowInd][colInd]
        else:
            return None

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # given an `m x n 2d integer array` matrix and in an `integer` target.
        # each row in matrix is sorted in ascending order.
        # the first integer of every row is greater than the last integer of the previous row.
        # return true if target exists within matrix or false otherwise.

        # write a solution that runs in O(log (m * n)), or basically log(n) time

        rows = len(matrix) # rows count
        cols = len(matrix[0]) # cols count
        l,r = 0,rows * cols

        middle = r // 2
        mVal = self.intoVal(middle,rows,cols,matrix)

        while mVal != None:
            print(mVal)
            oldM = middle
            if target < mVal :
                # go left
                r = middle
                middle = (r + l) // 2
                mVal = self.intoVal(middle,rows,cols,matrix)

            elif target > mVal:
                # go right
                l = middle
                middle = (r + l) // 2
                mVal = self.intoVal(middle,rows,cols,matrix)

            else:
                return True
            
            if oldM == middle:
                print("loop false")
                break

        print("outside false")
        return False


        
        