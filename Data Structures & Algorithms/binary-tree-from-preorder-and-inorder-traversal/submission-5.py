# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.head = 0
        indx = {v:i for i,v in enumerate(inorder)}

        def builder (l,r):
            if l > r:
                return None
            
            val = preorder[self.head]
            ind = indx[val]

            root = TreeNode(val)

            self.head += 1

            root.left = builder(l,ind-1)
            root.right = builder(ind+1,r)
            
            return root

        return builder(0,len(inorder)-1)