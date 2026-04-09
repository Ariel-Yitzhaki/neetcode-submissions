# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, n):
            if root is None:
                return 0
            
            if root.val >= n:
                return helper(root.left, root.val) + helper(root.right, root.val) + 1
            else:
                return helper(root.left, n) + helper(root.right, n)
        
        return helper(root, -101)
