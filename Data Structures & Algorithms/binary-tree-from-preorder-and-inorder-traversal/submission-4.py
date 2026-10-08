# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # HASHMAP of [ value : index ] for values in inorder array.
        index = { v:i for i,v in enumerate(inorder)}
        self.head = 0

        def builder(l,r):

            if l > r:
                return None

            val = preorder[self.head]

            ind = index[val]
            node = TreeNode(val)

            self.head += 1

            node.left = builder(l, ind - 1)
            node.right = builder(ind + 1, r)

            return node
        
        return builder(0,len(preorder)-1)


          



