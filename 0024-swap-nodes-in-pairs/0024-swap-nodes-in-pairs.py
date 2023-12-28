# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            # 앞 뒤 swap
            temp = head.next
            head.next = temp.next #1->3
            temp.next = head #2->1
            
            prev.next = temp # head를 새롭게 지정
            
            head = head.next
            prev = prev.next.next
            
        return root.next