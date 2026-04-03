"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lst1 = head
        
        if head is None:
            return None

        while lst1:
            lst2 = Node(lst1.val)
            lst2.next = lst1.next
            lst1.next = lst2
            lst1 = lst2.next
        
        new_head = head.next
        lst1 = head      

        while lst1:
            if lst1.random:
                lst1.next.random = lst1.random.next
            lst1 = lst1.next.next
        
        lst1 = head

        while lst1:
            lst2 = lst1.next
            lst1.next = lst2.next
            if lst2.next:
                lst2.next = lst2.next.next
            lst1 = lst1.next
    
        return new_head
        