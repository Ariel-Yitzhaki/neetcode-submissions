# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        firsthalf, secondhalf = head, head.next

        while secondhalf and secondhalf.next:
            firsthalf = firsthalf.next
            secondhalf = secondhalf.next.next

        second = firsthalf.next
        prev = firsthalf.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp  

        first = head

        while prev:
            temp1 = first.next
            temp2 = prev.next
            first.next = prev
            first = temp1
            prev.next = temp1
            prev = temp2
        
