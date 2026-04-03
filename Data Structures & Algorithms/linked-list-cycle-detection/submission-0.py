# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = defaultdict(int)
        index = 1

        while head:
            if hashmap[head] != 0:
                return True
            hashmap[head] = index
            head = head.next
            index += 1
        return False
         