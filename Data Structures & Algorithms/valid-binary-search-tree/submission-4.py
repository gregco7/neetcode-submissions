# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
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



        
        
       

        