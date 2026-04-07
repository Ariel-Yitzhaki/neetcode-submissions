# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        m = [0]
        self.help(root, m)
        return m[0]
        
    def help(self, root, m) -> int:
        if root is None:
            return 0
        left = self.help(root.left, m) 
        right = self.help(root.right, m)
        m[0] = max(m[0], left + right)
        return 1 + max(left, right)

