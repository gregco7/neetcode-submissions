# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        lvls = [[root]]
        curr = 0

        while curr < len(lvls):
            #augment our list
            nxtLvl = []
            for index,node in enumerate(lvls[curr]):
                
                # ...
                if node.left:
                    nxtLvl.append(node.left)
                if node.right:
                    nxtLvl.append(node.right)

                lvls[curr][index] = node.val
            if nxtLvl:
                lvls.append(nxtLvl)
            curr += 1
        
        return lvls

        