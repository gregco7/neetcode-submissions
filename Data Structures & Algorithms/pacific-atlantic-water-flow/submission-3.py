class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows,cols = len(heights),len(heights[0])
        pac,atl = set(),set()

        # DFS ACROSS EACH BORDER TO ADD TOUCHING ISLANDS TO PASSED SET (col/atl)

        def dfs(row,col,approved,prevH):

            # return if outside bounds or if previous height is greater than current
            if (row,col) in approved or ((row < 0) or (row > rows-1)) or ((col < 0) or (col > cols-1)) or prevH > heights[row][col]:
                return

            h = heights[row][col]
            approved.add((row,col))

            dfs(row-1,col,approved,h)
            dfs(row+1,col,approved,h)
            dfs(row,col-1,approved,h)
            dfs(row,col+1,approved,h)

        # TOP (PAC) / BOTTOM (ATL) WAVE
        for col in range (cols):
            dfs(0,col,pac,0)
            dfs(rows-1,col,atl,0)

        # LEFT (PAC) / RIGHT (ATL) WAVE
        for row in range (rows):
            dfs(row,0, pac,0)
            dfs(row, cols-1, atl,0)

        # RETURN RESULT
        return [[v[0],v[1]] for v in (pac & atl)]

        