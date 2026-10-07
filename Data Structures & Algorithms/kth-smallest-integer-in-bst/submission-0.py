# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []

        def dfs (node):
            if node:
            
                if node.left: # left first
                    num = dfs(node.left)

                nodes.append(node)

                if node.right:
                    num = dfs(node.right)
                
        dfs(root)
        return nodes[k-1].val
            
            

            





        