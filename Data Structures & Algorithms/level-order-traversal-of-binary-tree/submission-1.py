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
        new.append([q[0][0].val])
        while q:
            nodes = q.popleft()
            temp = []
            temp2 = []
            for node in nodes:
                if node.left:
                    temp2.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    temp2.append(node.right)
                    temp.append(node.right.val)
            if temp:
                new.append(temp)
                q.append(temp2)
        return new           
