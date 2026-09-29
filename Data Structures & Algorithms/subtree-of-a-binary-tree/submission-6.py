# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self,s,t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not (root and subRoot):
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root,subRoot):
                return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        



