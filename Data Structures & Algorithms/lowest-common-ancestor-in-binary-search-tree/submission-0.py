# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if root == p or root == q:
            return root

        if not root or (not (root.left or root.right)):
            return False

        lst = [root,root.left,root.right]

        if (p in lst) and (q in lst):
            return root

        searchL = self.lowestCommonAncestor(root.left, p, q)
        searchR = self.lowestCommonAncestor(root.right, p, q)

        if searchL and searchR:
            return root
        
        return searchL if searchL else searchR




