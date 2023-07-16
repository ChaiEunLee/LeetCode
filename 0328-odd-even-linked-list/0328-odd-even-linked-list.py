# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        fhead = first = head
        shead = second = head.next
        
        while second and second.next:
            first.next = first.next.next
            second.next = second.next.next
            
            first = first.next
            second = second.next
            
        first.next = shead
        
        return fhead