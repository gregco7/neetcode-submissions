# DFS SOLUTION

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.res = 0
        rowLen = len(grid[0])
        colLen = len(grid)
        visitedSet = set() # row , column

        # after finding a 1, navigate until you can't navigate anymore,
        # switching the previous 1's to zeros.

        def dfs(i,j,prev):
            val = grid[i][j]
            visitedSet.add((i,j))
            
            if val == "1" and prev != "1":
                self.res += 1

            # dfs across valid neighbors

            # UP
            if i > 0 and not ((i-1,j) in visitedSet) and grid[i-1][j] == "1":
                dfs(i-1,j,val)
            # DOWN
            if (i < colLen - 1) and not ((i+1,j) in visitedSet) and grid[i+1][j] == "1":
                dfs(i+1,j,val)
            # LEFT
            if (j > 0) and not ((i,j-1) in visitedSet) and grid[i][j-1] == "1":
                dfs(i,j-1,val)
            # RIGHT
            if (j < rowLen - 1) and not ((i,j+1) in visitedSet) and grid[i][j+1] == "1":
                dfs(i,j+1,val)

        for i in range (colLen):
            for j in range(rowLen):
                if grid[i][j] == "1" and not (i,j) in visitedSet:
                    dfs(i,j,"0")

        return self.res

        