# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        odd = head
        evenhead = even = head.next

        while even and even.next:
            odd.next, even.next  = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        odd.next = evenhead
        
        return head
            