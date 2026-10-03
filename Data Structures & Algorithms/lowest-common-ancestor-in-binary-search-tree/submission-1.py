# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root
        
        #then only two cases, both values are greater than root.val
        # or both values are less than root.val

        if (p.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        return self.lowestCommonAncestor(root.right,p,q)
            