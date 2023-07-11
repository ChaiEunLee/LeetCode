# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #(asis) prev -> a -> b -> b.next
        #(tobe) prev -> b -> a -> b.next
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            b = head.next

            head.next = b.next
            b.next = head

            prev.next = b

            #init
            prev = prev.next.next
            head = head.next
 
        return root.next