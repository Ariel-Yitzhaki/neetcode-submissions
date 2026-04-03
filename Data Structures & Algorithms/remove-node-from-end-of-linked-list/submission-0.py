# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hashmap = {}
        curr = head
        index = 0

        while curr:
            hashmap[index] = curr
            curr = curr.next
            index += 1
        
        hashmap[index] = None 

        if index - n == 0:
            return head.next
        
        hashmap[index - n] = None
        hashmap[index - n - 1].next = hashmap[index - n + 1]

        return head
            