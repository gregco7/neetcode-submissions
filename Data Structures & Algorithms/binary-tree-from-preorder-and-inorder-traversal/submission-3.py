# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # HASHMAP of [ value : index ] for values in inorder array.
        index = {v:i for i,v in enumerate(inorder)}
        self.pre = 0

        def build (l,r):
            if l > r:
                return None
            
            val = preorder[self.pre]
            self.pre += 1
            mid = index[val]

            node = TreeNode(val)
            node.left = build (l, mid-1) # inclusive, inclusive 
            node.right = build(mid+1, r) # inclusive, inclusive

            return node

        return build(0,len(preorder)-1)



          



