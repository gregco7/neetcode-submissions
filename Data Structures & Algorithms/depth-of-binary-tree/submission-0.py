# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #edge case
        if not root:
            return 0;

        l,r = root.left, root.right
        
        if l and r:
            
            return 1 + max(self.maxDepth(l),self.maxDepth(r))
        elif l:
            return 1 + self.maxDepth(l)
        elif r:
            return 1 + self.maxDepth(r)
        
        return 1

        

        

        