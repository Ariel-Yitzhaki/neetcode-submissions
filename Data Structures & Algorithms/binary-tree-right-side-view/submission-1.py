# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque()
        q.append([root])
        new_q = []
        new_q.append(root.val)
        while q:
            node = q.popleft()
            temp = []
            for n in node:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            
            if temp:
                q.append(temp)
                new_q.append(q[0][-1].val)
        return new_q