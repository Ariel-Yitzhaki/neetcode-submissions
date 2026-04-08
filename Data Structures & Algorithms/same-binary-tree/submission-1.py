# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        
        sq = []
        sp = []

        sq.append(q) 
        sp.append(p)

        while sq and sp:
            nodeQ = sq.pop()
            nodeP = sp.pop()
            
            if nodeQ.val != nodeP.val:
                return False

            if nodeQ.left and nodeP.left:
                sq.append(nodeQ.left)
                sp.append(nodeP.left)
            elif (nodeQ.left is None) != (nodeP.left is None):
                return False

            if nodeQ.right and nodeP.right:
                sq.append(nodeQ.right)
                sp.append(nodeP.right)
            elif (nodeQ.right is None) != (nodeP.right is None):
                return False
        if (sq is None) != (sp is None):
            return False
        return True
