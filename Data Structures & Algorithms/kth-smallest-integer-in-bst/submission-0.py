# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ind = 0

        def dfs(root, k):
            nonlocal ind
    
            if root is None:
                return 0
            
            left = dfs(root.left, k)
            if left != 0:
                return left
            ind += 1
            if k == ind:
                return root.val
            right = dfs(root.right, k)

            return right + left
        
        return dfs(root, k)
        