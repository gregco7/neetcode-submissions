# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# OLD SOLUTION BELOW, before cleanups that addressed
#   1. Extra memory from using lists to outline ranges instead of l,r
#   2. Redunant 'return True' statements that could be merged into one case instead of addressed seperately

"""
def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Left: mod range to (_, val)
        # Right: mod range to (val, _)
        def dfs(root,whitelist):

            if not root: return True
            if not (whitelist[0] < root.val < whitelist[1]):
                return False

            lrange = [whitelist[0],root.val]
            rrange = [root.val, whitelist[1]]

            if root.left or root.right:
                return dfs (root.left,lrange) and dfs (root.right, rrange)

            return True

        inf = float("infinity")
        ninf = float("-infinity")

        return dfs(root, [ninf,inf])
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Left: mod range to (_, val)
        # Right: mod range to (val, _) 
        def dfs(root,l,r):

            if not root: return True
            if not (l < root.val < r):
                return False

            return dfs (root.left,l,root.val) and dfs (root.right, root.val,r)
            
        inf = float("infinity")
        ninf = float("-infinity")

        return dfs(root, ninf, inf)



        
        
       

        