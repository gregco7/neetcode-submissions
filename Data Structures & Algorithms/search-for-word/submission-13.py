class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rowLen = len(board)
        colLen = len(board[0])
        charSet = set()

        def dfs (r,c,l):
            if l == len(word):
                return True
            
            look = word[l]

            # restrict up on row = 0
            # restrict down on row = rowLen - 1
            # restrict left on col = 0
            # restrict right on col = colLen - 1

            # look rows up, down
            charSet.add((r,c))
            if r > 0 and (board[r-1][c] == look) and not ((r-1,c) in charSet):
                if dfs(r-1,c,l+1):
                    return True
            if (r < rowLen - 1) and (board[r+1][c] == look) and not ((r+1,c) in charSet):
                if dfs(r+1,c,l+1):
                    return True

            # look cols left, right
            if c > 0 and (board[r][c-1] == look) and not ((r,c-1) in charSet):
                if dfs(r,c-1,l+1):
                    return True
            if (c < colLen - 1) and (board[r][c+1] == look) and not ((r,c+1) in charSet):
                if dfs(r,c+1,l+1):
                    return True
            charSet.remove((r,c))

            return False

        strt = word[0]
        
        for i in range (len(board)):
            for j in range(len(board[i])):
                if board[i][j] == strt:
                    if dfs(i,j,1): 
                        return True

        return False





        