# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
    
        q = deque()
        q.append([root])
        new = []
        
        while q:
            nodes = q.popleft()
            new.append([n.val for n in nodes])
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                q.append(temp)
        return new           
