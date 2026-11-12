class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # you are given a 9x9 sudoku board board
        # a sudoku board is valid if
        # 1. each row must contain the digits 1-9 without duplicates
        # 2. each column must contain the digits 1-9 without duplicates
        # 3. each of nine 3x3 sub-boxes of the grid must contain the digits 1-9 without duplicates
        
        # Method 1
        # A set, with tuples (row,col,box,val)
        # We will insert 3 tuples for each val, with the other attributes receiving a -1
        # ex row tup for row 0, col 0, val 1 would be (0,-1,1,1). Calculate which box it is
        # attempting to insert into an equivalent val will result in false

        ourArr = [set(),set(),set()] # row, col, box

        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]

                box = (j // 3)

                if i > 2:
                    box += 3
                if i > 5:
                    box += 6
                    
                row,col,box = (i,val), (j,val), (box,val)
                if not (val == "."):
                    if (row in ourArr[0] or col in ourArr[1] or box in ourArr[2]):
                        print(row,col,box)
                        return False
                    else:
                        ourArr[0].add(row)
                        ourArr[1].add(col)
                        ourArr[2].add(box)
            
        return True


