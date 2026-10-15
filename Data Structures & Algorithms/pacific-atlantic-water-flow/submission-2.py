class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # row,col : pacific, atlantic 
        # e.g. 0,0 : true,false because 0,0 can reach pacific but not atlantic
        cellMap = {}

        # question: are heights[0][rowlen-1] & heights[collen-1][0] always approved?
        # I think so

        # Method: DFS

        rowLen = len(heights)
        colLen = len(heights[0])

        def dfs(row,col):
            cell = (row,col)
            cellVal = heights[row][col]

            if cell in cellMap:
                return cellMap[cell][0],cellMap[cell][1]
            
            PAC = (row == 0) or (col == 0)
            ATL = (row == (rowLen - 1)) or (col == colLen - 1)

            cellMap[cell] = (PAC,ATL)

            # retrieve up
            if not (PAC and ATL) and ((row > 0) and (cellVal >= heights[row-1][col])):
                foundPac, foundAtl = dfs(row-1,col)  
                PAC,ATL = PAC or foundPac, ATL or foundAtl
            
            # retrieve down
            if not (PAC and ATL) and ((row < rowLen - 1) and (cellVal >= heights[row+1][col])):
                foundPac, foundAtl = dfs(row+1,col)  
                PAC,ATL = PAC or foundPac, ATL or foundAtl
            
             # retrieve left
            if not (PAC and ATL) and ((col > 0) and (cellVal >= heights[row][col-1])):
                foundPac, foundAtl = dfs(row,col-1)  
                PAC,ATL = PAC or foundPac, ATL or foundAtl
            
            # retrieve right
            if not (PAC and ATL) and ((col < colLen - 1) and (cellVal >= heights[row][col+1])):
                foundPac, foundAtl = dfs(row,col+1)  
                PAC,ATL = PAC or foundPac, ATL or foundAtl

            cellMap[cell] = (PAC,ATL)
            return PAC,ATL
        
        for rowIndex in range(rowLen):
            for colIndex in range(colLen):
                cell = (rowIndex,colIndex)
                if not cell in cellMap:
                    # set our map to the very best dfs can find
                    dfs(rowIndex,colIndex)

       
        return [ [key[0],key[1]] for key,value in cellMap.items() if value == (True,True) ]
        



        



        