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
        def dfs(root,l,r):

            if not root: return True
            if not (l < root.val < r):
                return False

            return dfs (root.left,l,root.val) and dfs (root.right, root.val,r)
            
        inf = float("infinity")
        ninf = float("-infinity")

        return dfs(root, ninf, inf)



        
        
       

        